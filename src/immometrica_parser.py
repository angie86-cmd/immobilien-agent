import csv
from pathlib import Path
from typing import Any

import pandas as pd


EXPECTED_COLUMNS = {
    "ort",
    "stadt",
    "plz",
    "postleitzahl",
    "adresse",
    "titel",
    "kaufpreis",
    "preis",
    "kp",
    "wohnfläche",
    "fläche",
    "wohnfl.",
    "wohnfl",
    "m²",
    "roi (s)",
    "roi (i)",
    "rendite",
    "bruttorendite",
    "tage online",
    "aktiv",
    "datum",
    "inseratsdauer",
    "online seit",
    "hausgeld",
    "hg",
    "bj",
    "baujahr",
}

DELIMITERS = [";", ",", "\t"]


def score_columns(columns: list[str]) -> int:
    normalized = {str(column).strip().lower() for column in columns}
    return len(normalized.intersection(EXPECTED_COLUMNS))


def read_immometrica_csv(path: str | Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    path = Path(path)
    attempts: list[dict[str, Any]] = []

    for delimiter in DELIMITERS:
        try:
            df = pd.read_csv(
                path,
                sep=delimiter,
                encoding="utf-8-sig",
                dtype=str,
                engine="python",
                quoting=csv.QUOTE_MINIMAL,
                on_bad_lines="warn",
            )

            column_score = score_columns(list(df.columns))
            rows = len(df)
            columns = len(df.columns)

            attempt = {
                "delimiter": delimiter,
                "rows": rows,
                "columns": columns,
                "column_score": column_score,
                "error": None,
            }
            attempts.append(attempt)

            if column_score >= 4 and columns > 5:
                report = {
                    "status": "OK",
                    "encoding": "utf-8-sig",
                    "delimiter": delimiter,
                    "rows": rows,
                    "data_objects": rows,
                    "columns": columns,
                    "recognized_core_columns": column_score,
                    "bad_lines": 0,
                    "stable_column_count": True,
                    "attempts": attempts,
                }
                return df, report

        except Exception as exc:
            attempts.append(
                {
                    "delimiter": delimiter,
                    "rows": None,
                    "columns": None,
                    "column_score": 0,
                    "error": str(exc),
                }
            )

    best_attempt = max(attempts, key=lambda item: item["column_score"])

    error_report = {
        "status": "FEHLER",
        "message": "CSV konnte nicht robust als ImmoMetrica-Datei erkannt werden.",
        "best_attempt": best_attempt,
        "attempts": attempts,
    }

    raise ValueError(error_report)


def normalize_german_number(value: Any) -> float | None:
    if pd.isna(value):
        return None

    text = str(value).strip()

    if not text:
        return None

    text = (
        text.replace("€", "")
        .replace("%", "")
        .replace("m²", "")
        .replace("\xa0", "")
        .replace(" ", "")
    )

    # German format: 1.234,56
    if "," in text and "." in text:
        text = text.replace(".", "").replace(",", ".")

    # German decimal: 7,8
    elif "," in text:
        text = text.replace(",", ".")

    # Integer with thousands dot: 150.000
    elif "." in text and text.count(".") == 1:
        left, right = text.split(".")
        if len(right) == 3:
            text = left + right

    try:
        return float(text)
    except ValueError:
        return None