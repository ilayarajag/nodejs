from __future__ import annotations

import argparse
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from config.db_config import get_db_config
from scripts.extract import extract_rows
from scripts.load import load_rows
from scripts.transform import transform_rows


def run(input_csv: str | Path) -> int:
    extracted = extract_rows(input_csv)
    transformed = transform_rows(extracted)
    db = get_db_config()
    return load_rows(transformed, db=db, table="facts")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the sample ETL pipeline.")
    parser.add_argument(
        "--input",
        default=str(Path("data") / "sample_input.csv"),
        help="Path to input CSV (default: data/sample_input.csv)",
    )
    args = parser.parse_args()

    inserted = run(args.input)
    print(f"Loaded {inserted} rows.")


if __name__ == "__main__":
    main()

