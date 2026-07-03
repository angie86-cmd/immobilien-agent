from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.immometrica_parser import read_immometrica_csv


TEST_FILES = [
    {
        "name": "Hannover",
        "path": Path("tests/fixtures/raw/20260701_offers_Hannover.csv"),
        "expected_rows": 126,
        "expected_columns": 46,
    },
    {
        "name": "Leipzig",
        "path": Path("tests/fixtures/raw/20260702_offers_Leipzig.csv"),
        "expected_rows": 333,
        "expected_columns": 46,
    },
]


REQUIRED_COLUMNS = {
    "PLZ",
    "Ort",
    "Adresse",
    "Preis",
    "ROI (s)",
    "Tage online",
}


def run_parser_smoke_test() -> None:
    print("ImmoMetrica Parser Smoke Test")
    print(f"Repository root: {REPO_ROOT}")

    for test_file in TEST_FILES:
        file_path = REPO_ROOT / test_file["path"]

        print("=" * 80)
        print(f"Testing: {test_file['name']}")
        print(f"File: {file_path}")

        if not file_path.exists():
            raise FileNotFoundError(f"Missing test fixture: {file_path}")

        df, report = read_immometrica_csv(file_path)

        print("CSV-IMPORT-REPORT")
        print(f"status: {report['status']}")
        print(f"encoding: {report['encoding']}")
        print(f"delimiter: {report['delimiter']}")
        print(f"rows: {report['rows']}")
        print(f"data_objects: {report['data_objects']}")
        print(f"columns: {report['columns']}")
        print(f"recognized_core_columns: {report['recognized_core_columns']}")
        print(f"stable_column_count: {report['stable_column_count']}")

        assert report["status"] == "OK", report
        assert report["delimiter"] == ";", report
        assert report["columns"] == test_file["expected_columns"], report
        assert len(df) == test_file["expected_rows"], (
            f"Expected {test_file['expected_rows']} rows, got {len(df)}"
        )
        assert report["recognized_core_columns"] >= 8, report

        missing_columns = REQUIRED_COLUMNS.difference(set(df.columns))

        if missing_columns:
            raise AssertionError(
                f"Missing required columns in {test_file['name']}: {missing_columns}"
            )

        print(f"RESULT {test_file['name']}: OK")

    print("=" * 80)
    print("ALL PARSER SMOKE TESTS PASSED")


if __name__ == "__main__":
    run_parser_smoke_test()