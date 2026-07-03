"""Compare an Immobilien agent result with the generic liquidity audit."""

import argparse
from pathlib import Path
import sys
from typing import Sequence

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.liquidity_audit import (  # noqa: E402
    MANUAL_REVIEW_REASONS,
    run_liquidity_audit,
)


AGENT_REQUIRED_COLUMNS = {
    "dataset_label",
    "link_immometrica",
    "id",
    "ort",
    "adresse",
    "titel",
    "preis",
    "wohnflaeche",
    "roi_s",
    "tage_online",
    "score_vor_malus",
    "liquiditaets_malus",
    "score_final",
    "klasse",
    "agent_decision",
    "exclusion_reason",
    "risk_level",
    "next_step",
}

AUDIT_REQUIRED_COLUMNS = {
    "dataset_label",
    "link_immometrica",
    "ort",
    "adresse",
    "preis",
    "wohnflaeche",
    "roi_s",
    "tage_online",
    "liquiditaets_malus",
    "audit_kategorie",
    "manual_review_required",
}

COMPARISON_COLUMNS = [
    "dataset_label",
    "link_immometrica",
    "ort",
    "adresse",
    "titel",
    "preis",
    "wohnflaeche",
    "roi_s",
    "tage_online",
    "agent_decision",
    "agent_klasse",
    "score_vor_malus",
    "agent_liquiditaets_malus",
    "score_final",
    "exclusion_reason",
    "risk_level",
    "next_step",
    "audit_kategorie",
    "audit_liquiditaets_malus",
    "manual_review_required",
    "manual_review_reason",
    "validation_result",
]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare an agent output CSV with its liquidity audit."
    )
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--agent", required=True, type=Path)
    parser.add_argument("--audit", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary", type=Path)
    return parser.parse_args(argv)


def derive_default_audit_path(source_path: str | Path) -> Path:
    return REPO_ROOT / "reports" / f"{Path(source_path).stem}_liquidity_audit.csv"


def derive_default_output_path(source_path: str | Path) -> Path:
    return (
        REPO_ROOT
        / "reports"
        / f"{Path(source_path).stem}_agent_vs_liquidity_audit.csv"
    )


def derive_default_summary_path(source_path: str | Path) -> Path:
    return (
        REPO_ROOT
        / "reports"
        / f"{Path(source_path).stem}_agent_vs_liquidity_audit_summary.md"
    )


def parse_bool(value: object) -> bool:
    """Parse common German and English boolean representations."""
    if value is None or pd.isna(value):
        return False
    if isinstance(value, bool):
        return value
    text = str(value).strip().casefold()
    if text in {"true", "1", "yes", "ja", "wahr"}:
        return True
    if text in {"false", "0", "no", "nein", "falsch", ""}:
        return False
    return False


def is_agent_exclusion(row: pd.Series) -> bool:
    """Return whether decision or class identifies an agent exclusion."""
    decision = str(row.get("agent_decision", "") or "").casefold()
    agent_class = str(row.get("klasse", "") or "").casefold()
    return (
        "ausschließen" in decision
        or "ausschliessen" in decision
        or "exclude" in decision
        or "ausschliessen" in agent_class.replace("ß", "ss")
        or "❌" in agent_class
    )


def validate_required_columns(
    df: pd.DataFrame, required_columns: set[str], file_label: str
) -> None:
    missing = sorted(required_columns.difference(df.columns))
    if missing:
        raise ValueError(
            f"Required columns are missing from {file_label}: {', '.join(missing)}"
        )


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load one semicolon-delimited UTF-8-SIG report without type coercion."""
    return pd.read_csv(path, sep=";", encoding="utf-8-sig", dtype=str)


def ensure_liquidity_audit(
    source_path: str | Path, audit_path: str | Path | None = None
) -> tuple[pd.DataFrame, Path]:
    """Load the requested audit or create the default audit when absent."""
    source_path = Path(source_path).resolve()
    resolved_audit = (
        Path(audit_path).resolve()
        if audit_path is not None
        else derive_default_audit_path(source_path)
    )
    if resolved_audit.is_file():
        return load_csv(resolved_audit), resolved_audit
    if audit_path is not None:
        raise FileNotFoundError(f"Liquidity audit CSV not found: {resolved_audit}")
    return run_liquidity_audit(source_path, resolved_audit)


def _coalesce(frame: pd.DataFrame, first: str, second: str) -> pd.Series:
    return frame[first].combine_first(frame[second])


def build_comparison(agent: pd.DataFrame, audit: pd.DataFrame) -> pd.DataFrame:
    """Outer-join agent and audit data and classify every resulting row."""
    validate_required_columns(agent, AGENT_REQUIRED_COLUMNS, "agent output")
    validate_required_columns(audit, AUDIT_REQUIRED_COLUMNS, "liquidity audit")

    agent = agent[sorted(AGENT_REQUIRED_COLUMNS)].copy()
    audit = audit.copy()
    if "manual_review_reason" not in audit.columns:
        audit["manual_review_reason"] = audit["audit_kategorie"].map(
            MANUAL_REVIEW_REASONS
        )
    audit = audit[sorted(AUDIT_REQUIRED_COLUMNS | {"manual_review_reason"})].copy()
    agent["agent_excluded"] = agent.apply(is_agent_exclusion, axis=1)
    audit["manual_review_required"] = audit["manual_review_required"].map(parse_bool)

    agent = agent.rename(
        columns={
            "dataset_label": "agent_dataset_label",
            "ort": "agent_ort",
            "adresse": "agent_adresse",
            "preis": "agent_preis",
            "wohnflaeche": "agent_wohnflaeche",
            "roi_s": "agent_roi_s",
            "tage_online": "agent_tage_online",
            "klasse": "agent_klasse",
            "liquiditaets_malus": "agent_liquiditaets_malus",
        }
    )
    audit = audit.rename(
        columns={
            "dataset_label": "audit_dataset_label",
            "ort": "audit_ort",
            "adresse": "audit_adresse",
            "preis": "audit_preis",
            "wohnflaeche": "audit_wohnflaeche",
            "roi_s": "audit_roi_s",
            "tage_online": "audit_tage_online",
            "liquiditaets_malus": "audit_liquiditaets_malus",
        }
    )

    merged = agent.merge(
        audit,
        on="link_immometrica",
        how="outer",
        indicator=True,
        validate="one_to_one",
    )
    for output_name in (
        "dataset_label",
        "ort",
        "adresse",
        "preis",
        "wohnflaeche",
        "roi_s",
        "tage_online",
    ):
        merged[output_name] = _coalesce(
            merged, f"agent_{output_name}", f"audit_{output_name}"
        )

    def classify(row: pd.Series) -> str:
        if row["_merge"] == "right_only":
            return "MISSING_IN_AGENT_OUTPUT"
        if row["_merge"] == "left_only":
            return "MISSING_IN_LIQUIDITY_AUDIT"
        category = str(row.get("audit_kategorie", "") or "")
        if bool(row["agent_excluded"]):
            if category.startswith("Altinserat-Renditefalle"):
                return "EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK"
            if category.startswith("Altinserat-Risiko"):
                return "EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK"
            if category.startswith("Stale Listing Due Diligence"):
                return "NEEDS_MANUAL_CONFIRMATION"
            if category == "möglicher False Negative":
                return "POTENTIAL_FALSE_NEGATIVE"
            if not bool(row["manual_review_required"]):
                return "LIKELY_VALID_EXCLUSION"
            return "NEEDS_MANUAL_CONFIRMATION"
        if category.startswith("Altinserat"):
            return "NEEDS_DUE_DILIGENCE_STALE_LISTING"
        if bool(row["manual_review_required"]):
            return "NEEDS_DUE_DILIGENCE"
        return "OK"

    merged["validation_result"] = merged.apply(classify, axis=1)
    return merged[COMPARISON_COLUMNS]


def _markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    if df.empty:
        return "_Keine Objekte._"

    label_overrides = {
        "roi_s": "ROI",
        "tage_online": "Tage online",
        "score_final": "Score final",
        "agent_decision": "Agent decision",
        "audit_kategorie": "Audit category",
        "exclusion_reason": "Exclusion reason",
        "link_immometrica": "Link",
        "validation_result": "Validation result",
        "count": "Count",
    }
    labels = [
        label_overrides.get(column, column.replace("_", " ").title())
        for column in columns
    ]
    lines = [
        "| " + " | ".join(labels) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for values in df[columns].itertuples(index=False, name=None):
        cells = []
        for value in values:
            text = "" if pd.isna(value) else str(value)
            cells.append(text.replace("|", "\\|").replace("\n", " "))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_markdown_summary(
    comparison: pd.DataFrame,
    summary_path: str | Path,
    source_path: str | Path,
    agent_path: str | Path,
    audit_path: str | Path,
) -> Path:
    """Write a deterministic Markdown summary of conflicts and review cases."""
    summary_path = Path(summary_path).resolve()
    counts = (
        comparison["validation_result"]
        .value_counts()
        .rename_axis("validation_result")
        .reset_index(name="count")
        .sort_values("validation_result")
    )
    detail_columns = [
        "ort",
        "adresse",
        "preis",
        "roi_s",
        "tage_online",
        "score_final",
        "agent_decision",
        "audit_kategorie",
        "exclusion_reason",
        "link_immometrica",
    ]
    false_negatives = comparison[
        comparison["validation_result"] == "POTENTIAL_FALSE_NEGATIVE"
    ]
    stale_supported = comparison[
        comparison["validation_result"].isin(
            {
                "EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK",
                "EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK",
            }
        )
    ]
    stale_high_roi = comparison[
        comparison["audit_kategorie"].fillna("").str.startswith(
            "Altinserat-Renditefalle"
        )
    ]
    due_diligence = comparison[
        comparison["validation_result"].isin(
            {
                "NEEDS_DUE_DILIGENCE",
                "NEEDS_DUE_DILIGENCE_STALE_LISTING",
                "NEEDS_MANUAL_CONFIRMATION",
            }
        )
    ]
    content = f"""# Agent Validation Summary

## Input files

- Source CSV: `{Path(source_path).resolve()}`
- Agent output: `{Path(agent_path).resolve()}`
- Liquidity audit: `{Path(audit_path).resolve()}`

## Result overview

{_markdown_table(counts, ["validation_result", "count"])}

## Potential False Negatives

{_markdown_table(false_negatives, detail_columns)}

## Exclusions supported by stale listing risk

{_markdown_table(stale_supported, detail_columns)}

## Stale high-ROI traps

{_markdown_table(stale_high_roi, detail_columns)}

## Needs Due Diligence

{_markdown_table(due_diligence, detail_columns)}

## Interpretation

- **POTENTIAL_FALSE_NEGATIVE**: Der Agent könnte zu aggressiv gefiltert haben.
- **EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK**: Der Ausschluss ist wahrscheinlich nachvollziehbar, weil alte Angebote mit hoher ROI oft ernste verdeckte Risiken haben.
- **EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK**: Der Ausschluss wird durch das Altinserat-Risiko gestützt.
- **NEEDS_DUE_DILIGENCE_STALE_LISTING**: Das Objekt ist nicht automatisch ausgeschlossen, seine lange Inseratsdauer verlangt aber starke Vorsicht.
- **NEEDS_DUE_DILIGENCE / NEEDS_MANUAL_CONFIRMATION**: Risiko oder Ausschlussgrund muss manuell bestätigt werden.
- **LIKELY_VALID_EXCLUSION**: Der Ausschluss ist wahrscheinlich mit dem Liquiditäts-Audit konsistent.
- **OK**: Es besteht kein Konflikt zwischen Agentenentscheidung und Audit.

`manual_review_required` ist ein Prüfhinweis, keine Aussage, dass der Agent falsch lag.
"""
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(content, encoding="utf-8")
    return summary_path


def print_console_summary(
    comparison: pd.DataFrame,
    source_path: Path,
    agent_path: Path,
    audit_path: Path,
    output_path: Path,
    summary_path: Path,
    audit_rows: int,
    agent_rows: int,
) -> None:
    print("Agent Result Validation")
    print(f"Source CSV path: {source_path}")
    print(f"Agent output path: {agent_path}")
    print(f"Liquidity audit path: {audit_path}")
    print(f"Comparison output path: {output_path}")
    print(f"Summary output path: {summary_path}")
    print(f"Total source/audit rows: {audit_rows}")
    print(f"Total agent rows: {agent_rows}")
    print(f"Total matched rows: {(~comparison['validation_result'].str.startswith('MISSING_')).sum()}")
    print(f"Missing in agent output: {(comparison['validation_result'] == 'MISSING_IN_AGENT_OUTPUT').sum()}")
    print(f"Missing in liquidity audit: {(comparison['validation_result'] == 'MISSING_IN_LIQUIDITY_AUDIT').sum()}")
    print("\nDistribution of validation_result:")
    print(comparison["validation_result"].value_counts().to_string())
    potential = comparison[
        comparison["validation_result"] == "POTENTIAL_FALSE_NEGATIVE"
    ]
    due_diligence = comparison[
        comparison["validation_result"].str.startswith("NEEDS_")
    ]
    print(f"\nPOTENTIAL_FALSE_NEGATIVE: {len(potential)}")
    print(f"Needs due diligence/manual confirmation: {len(due_diligence)}")
    print("Manual review required is a review flag, not a statement that the agent was wrong.")
    if not potential.empty:
        columns = [
            "ort",
            "adresse",
            "preis",
            "roi_s",
            "tage_online",
            "score_final",
            "agent_decision",
            "audit_kategorie",
            "exclusion_reason",
            "link_immometrica",
        ]
        print("\nPotential false negatives:")
        print(potential[columns].to_string(index=False))


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    source_path = args.source.resolve()
    agent_path = args.agent.resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"ImmoMetrica source CSV not found: {source_path}")
    if not agent_path.is_file():
        raise FileNotFoundError(f"Agent output CSV not found: {agent_path}")

    audit, audit_path = ensure_liquidity_audit(source_path, args.audit)
    agent = load_csv(agent_path)
    comparison = build_comparison(agent, audit)
    output_path = (
        args.output.resolve() if args.output else derive_default_output_path(source_path)
    )
    summary_path = (
        args.summary.resolve()
        if args.summary
        else derive_default_summary_path(source_path)
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(output_path, sep=";", encoding="utf-8-sig", index=False)
    write_markdown_summary(
        comparison, summary_path, source_path, agent_path, audit_path
    )
    print_console_summary(
        comparison,
        source_path,
        agent_path,
        audit_path,
        output_path,
        summary_path,
        len(audit),
        len(agent),
    )


if __name__ == "__main__":
    main()
