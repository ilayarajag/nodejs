from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable


def extract_rows(input_csv: str | Path) -> Iterable[Dict[str, str]]:
  path = Path(__file__).resolve().parent.parent / "data" / "sample_input.csv"
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield dict(row)

