"""Audit ImmoMetrica exports for liquidity and stale-listing risks."""

import argparse
from pathlib import Path
import re
import sys
from typing import Sequence

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.immometrica_parser import (  # noqa: E402
    normalize_german_number,
    read_immometrica_csv,
)


REQUIRED_COLUMNS = {
    "Details",
    "PLZ",
    "Ort",
    "Adresse",
    "Titel",
    "Preis",
    "Wfl.",
    "ROI (s)",
    "Tage online",
}

COLUMN_MAPPINGS = {
    "Details": "details",
    "PLZ": "plz",
    "Ort": "ort",
    "Adresse": "adresse",
    "Titel": "titel",
    "Preis": "preis",
    "Wfl.": "wohnflaeche",
    "ROI (s)": "roi_s",
    "ROI (i)": "roi_i",
    "Tage online": "tage_online",
    "Hausgeld": "hausgeld",
    "Zustand": "zustand",
    "Trend": "trend",
    "Cash-<br>flow": "cashflow",
}

NUMERIC_COLUMNS = {
    "Preis",
    "Wfl.",
    "ROI (s)",
    "ROI (i)",
    "Tage online",
    "Hausgeld",
    "Cash-<br>flow",
}

MANUAL_REVIEW_CATEGORIES = {
    "Altinserat-Renditefalle: hohe ROI, aber sehr lange online",
    "Altinserat-Risiko: sehr lange online",
    "Stale Listing Due Diligence: alt, aber eventuell prüfbar",
}

MANUAL_REVIEW_REASONS = {
    "Altinserat-Renditefalle: hohe ROI, aber sehr lange online": "stale_high_roi_risk",
    "Altinserat-Risiko: sehr lange online": "stale_listing_risk",
    "Stale Listing Due Diligence: alt, aber eventuell prüfbar": "stale_due_diligence",
    "kein Liquiditätsrisiko": "no_liquidity_issue",
    "Datenmangel: ROI fehlt": "roi_missing",
    "berechtigt schwach: ROI unter Hard Cutoff": "weak_roi",
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for one ImmoMetrica input file."""
    parser = argparse.ArgumentParser(
        description="Audit liquidity penalties in an ImmoMetrica CSV export."
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to an ImmoMetrica CSV export.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional report path (default: reports/<input stem>_liquidity_audit.csv).",
    )
    return parser.parse_args(argv)


def detect_dataset_label(input_path: str | Path, df: pd.DataFrame) -> str:
    """Detect the dataset label, preferring the city encoded in the filename."""
    stem = Path(input_path).stem
    match = re.fullmatch(r"\d{8}_offers_(.+)", stem, flags=re.IGNORECASE)
    if match and match.group(1).strip():
        return match.group(1).strip()

    if "Ort" in df.columns:
        locations = df["Ort"].dropna().astype(str).str.strip()
        locations = locations[locations != ""]
        if not locations.empty:
            return locations.value_counts().index[0]

    return "unknown_dataset"


def calculate_liquidity_malus(days_online: float | None) -> int:
    """Calculate the liquidity penalty for an offer's time online."""
    if days_online is None or pd.isna(days_online):
        return 0
    if days_online < 14:
        return 0
    if days_online <= 60:
        return -5
    if days_online <= 180:
        return -15
    return -30


def classify_liquidity_bucket(days_online: float | None) -> str:
    """Return a readable bucket for an offer's time online."""
    if days_online is None or pd.isna(days_online):
        return "unbekannt"
    if days_online < 14:
        return "<14 Tage"
    if days_online <= 60:
        return "14–60 Tage"
    if days_online <= 180:
        return "61–180 Tage"
    return ">180 Tage"


def classify_audit(row: pd.Series) -> str:
    """Classify whether a liquidity penalty merits closer inspection."""
    roi = row["roi_s"]
    malus = row["liquiditaets_malus"]
    days_online = row["tage_online"]

    if roi is None or pd.isna(roi):
        return "Datenmangel: ROI fehlt"
    if malus == 0:
        return "kein Liquiditätsrisiko"
    if roi < 4.0:
        return "berechtigt schwach: ROI unter Hard Cutoff"
    if days_online is not None and not pd.isna(days_online) and days_online > 180:
        if roi >= 6.0:
            return "Altinserat-Renditefalle: hohe ROI, aber sehr lange online"
        return "Altinserat-Risiko: sehr lange online"
    if (
        days_online is not None
        and not pd.isna(days_online)
        and 61 <= days_online <= 180
        and roi >= 6.0
    ):
        return "Stale Listing Due Diligence: alt, aber eventuell prüfbar"
    return "prüfen"


def validate_required_columns(df: pd.DataFrame) -> None:
    """Raise an informative error if critical source columns are absent."""
    missing = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Required columns are missing: {', '.join(missing)}")


def build_audit_dataframe(df: pd.DataFrame, dataset_label: str) -> pd.DataFrame:
    """Extract, normalize, and classify the fields used by the audit."""
    validate_required_columns(df)
    audit = pd.DataFrame(index=df.index)
    audit["dataset_label"] = dataset_label

    for source_name, output_name in COLUMN_MAPPINGS.items():
        if source_name not in df.columns:
            audit[output_name] = pd.NA
        elif source_name in NUMERIC_COLUMNS:
            audit[output_name] = df[source_name].map(normalize_german_number)
        else:
            audit[output_name] = df[source_name]

    audit["link_immometrica"] = audit["details"]
    audit["online_bucket"] = audit["tage_online"].map(classify_liquidity_bucket)
    audit["liquiditaets_malus"] = audit["tage_online"].map(
        calculate_liquidity_malus
    )
    audit["audit_kategorie"] = audit.apply(classify_audit, axis=1)
    audit["manual_review_required"] = audit["audit_kategorie"].isin(
        MANUAL_REVIEW_CATEGORIES
    )
    audit["manual_review_reason"] = audit["audit_kategorie"].map(
        MANUAL_REVIEW_REASONS
    )
    return audit


def _print_distribution(title: str, values: pd.Series) -> None:
    print(f"\n{title}")
    print(values.value_counts(dropna=False).to_string())


def print_summary(audit: pd.DataFrame) -> None:
    """Print aggregate audit results and compact manual-review candidates."""
    print(f"\nTotal number of objects: {len(audit)}")
    _print_distribution("Distribution of online buckets:", audit["online_bucket"])
    _print_distribution(
        "Distribution of liquidity penalties:", audit["liquiditaets_malus"]
    )
    _print_distribution("Distribution of audit categories:", audit["audit_kategorie"])

    review = audit[audit["manual_review_required"]]
    print(f"\nObjects requiring manual review: {len(review)}")
    print("Manual review required does not automatically mean false negative.")
    print(
        "For old listings, the exclusion may be justified but its risk reason "
        "should be documented."
    )
    if not review.empty:
        columns = [
            "ort",
            "adresse",
            "preis",
            "wohnflaeche",
            "roi_s",
            "tage_online",
            "liquiditaets_malus",
            "audit_kategorie",
            "manual_review_reason",
        ]
        print(review[columns].to_string(index=False))


def run_liquidity_audit(
    input_path: str | Path, output_path: str | Path | None = None
) -> tuple[pd.DataFrame, Path]:
    """Build and export an audit, returning its DataFrame and resolved path."""
    input_path = Path(input_path).resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"ImmoMetrica input file not found: {input_path}")

    resolved_output = (
        Path(output_path).resolve()
        if output_path is not None
        else REPO_ROOT / "reports" / f"{input_path.stem}_liquidity_audit.csv"
    )
    source, _ = read_immometrica_csv(input_path)
    dataset_label = detect_dataset_label(input_path, source)
    audit = build_audit_dataframe(source, dataset_label)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    audit.to_csv(resolved_output, sep=";", encoding="utf-8-sig", index=False)
    return audit, resolved_output


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    input_path = args.input.resolve()
    output_path = (
        args.output.resolve()
        if args.output
        else REPO_ROOT / "reports" / f"{input_path.stem}_liquidity_audit.csv"
    )

    if not input_path.is_file():
        raise FileNotFoundError(f"ImmoMetrica input file not found: {input_path}")

    source, import_report = read_immometrica_csv(input_path)
    dataset_label = detect_dataset_label(input_path, source)
    audit, output_path = run_liquidity_audit(input_path, output_path)

    print("ImmoMetrica Liquidity Audit")
    print(f"Input path: {input_path}")
    print(f"Dataset label: {dataset_label}")
    print(f"Output path: {output_path}")
    print("\nCSV import report")
    for key in (
        "status",
        "encoding",
        "delimiter",
        "rows",
        "data_objects",
        "columns",
        "recognized_core_columns",
        "stable_column_count",
    ):
        print(f"{key}: {import_report[key]}")
    print_summary(audit)


if __name__ == "__main__":
    main()
