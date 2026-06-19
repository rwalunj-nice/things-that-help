import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def _state_file() -> Path:
    return Path.cwd() / "state.json"


def load_last_scan_at() -> datetime:
    sf = _state_file()
    if not sf.exists():
        return datetime.now(timezone.utc) - timedelta(hours=24)
    data = json.loads(sf.read_text())
    return datetime.fromisoformat(data["last_scan_at"])


def save_last_scan_at(dt: datetime) -> None:
    sf = _state_file()
    data = {}
    if sf.exists():
        data = json.loads(sf.read_text())
    data["last_scan_at"] = dt.isoformat()
    sf.write_text(json.dumps(data, indent=2))
