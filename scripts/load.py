from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Dict, Iterable

from config.db_config import DBConfig


def _ensure_parent_dir(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)


def load_rows(rows: Iterable[Dict[str, object]], db: DBConfig, table: str = "facts") -> int:
    if db.kind != "sqlite":
        raise ValueError(f"Unsupported DB_KIND={db.kind!r}. Only 'sqlite' is wired by default.")

    db_path = Path(db.sqlite_path)
    _ensure_parent_dir(db_path)

    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table} (
              id INTEGER,
              name TEXT,
              amount REAL,
              ingested_at TEXT
            )
            """
        )

        inserted = 0
        for r in rows:
            conn.execute(
                f"INSERT INTO {table} (id, name, amount, ingested_at) VALUES (?, ?, ?, ?)",
                (
                    r.get("id"),
                    r.get("name"),
                    r.get("amount"),
                    r.get("ingested_at"),
                ),
            )
            inserted += 1
        conn.commit()
        return inserted
    finally:
        conn.close()

