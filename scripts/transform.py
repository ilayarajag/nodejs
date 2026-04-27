from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, Iterable, Iterator


def transform_rows(rows: Iterable[Dict[str, str]]) -> Iterator[Dict[str, object]]:
    """
    Example transform:
    - normalize types (id -> int, amount -> float)
    - add ingestion timestamp
    """
    ingested_at = datetime.now(timezone.utc).isoformat()
    for r in rows:
        out: Dict[str, object] = dict(r)
        if "id" in out and out["id"] not in (None, ""):
            out["id"] = int(str(out["id"]))
        if "amount" in out and out["amount"] not in (None, ""):
            out["amount"] = float(str(out["amount"]))
        out["ingested_at"] = ingested_at
        yield out

