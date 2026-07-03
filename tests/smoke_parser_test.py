from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.immometrica_parser import read_immometrica_csv


RAW_FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "raw"
CSV_PATTERN = "*_offers_*.csv"
EXPECTED_COLUMNS = 46


REQUIRED_COLUMNS = {
    "PLZ",
    "Ort",
    "Adresse",
    "Preis",
    "ROI (s)",
    "Tage online",
}


def discover_test_files() -> list[Path]:
    if not RAW_FIXTURE_DIR.is_dir():
        raise FileNotFoundError(f"Fixture directory not found: {RAW_FIXTURE_DIR}")

    csv_files = sorted(RAW_FIXTURE_DIR.glob(CSV_PATTERN))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_FIXTURE_DIR} "
            f"matching pattern {CSV_PATTERN}"
        )

    return csv_files


def run_parser_smoke_test() -> None:
    print("ImmoMetrica Parser Smoke Test")
    print(f"Repository root: {REPO_ROOT}")

    for file_path in discover_test_files():

        print("=" * 80)
        print(f"Testing: {file_path.name}")
        print(f"File: {file_path}")

        if not file_path.exists():
            raise FileNotFoundError(f"Missing test fixture: {file_path}")

        try:
            df, report = read_immometrica_csv(file_path)
        except Exception as exc:
            raise RuntimeError(f"Failed to parse CSV file: {file_path}") from exc

        print("CSV-IMPORT-REPORT")
        print(f"status: {report['status']}")
        print(f"encoding: {report['encoding']}")
        print(f"delimiter: {report['delimiter']}")
        print(f"rows: {report['rows']}")
        print(f"data_objects: {report['data_objects']}")
        print(f"columns: {report['columns']}")
        print(f"recognized_core_columns: {report['recognized_core_columns']}")
        print(f"stable_column_count: {report['stable_column_count']}")

        assert report["status"] == "OK", f"Unexpected parser status for {file_path}: {report}"
        assert report["delimiter"] == ";", f"Unexpected delimiter for {file_path}: {report}"
        assert report["rows"] > 0, f"CSV has zero rows: {file_path}"
        assert report["columns"] == EXPECTED_COLUMNS, (
            f"Expected {EXPECTED_COLUMNS} columns in {file_path}, "
            f"got {report['columns']}"
        )
        assert not df.empty, f"Parser output is empty for {file_path}"
        assert report["recognized_core_columns"] >= 8, (
            f"Too few recognized core columns for {file_path}: {report}"
        )

        missing_columns = REQUIRED_COLUMNS.difference(set(df.columns))

        if missing_columns:
            raise AssertionError(
                f"Missing required columns in {file_path}: {missing_columns}"
            )

        print(f"RESULT {file_path.name}: OK")

    print("=" * 80)
    print("ALL PARSER SMOKE TESTS PASSED")


if __name__ == "__main__":
    run_parser_smoke_test()
