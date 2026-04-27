from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class DBConfig:
    """
    Default to a local SQLite database so the project runs out-of-the-box.
    You can override with environment variables later (e.g., for Postgres).
    """

    kind: str = os.getenv("DB_KIND", "sqlite")
    sqlite_path: str = os.getenv("SQLITE_PATH", str(_PROJECT_ROOT / "data" / "warehouse.db"))


def get_db_config() -> DBConfig:
    cfg = DBConfig()
    if cfg.kind == "sqlite":
        p = Path(cfg.sqlite_path)
        if not p.is_absolute():
            p = _PROJECT_ROOT / p
        return DBConfig(kind=cfg.kind, sqlite_path=str(p))
    return cfg

