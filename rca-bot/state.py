import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

_STATE_FILE = Path(__file__).parent / "state.json"


def load_last_scan_at() -> datetime:
    if not _STATE_FILE.exists():
        return datetime.now(timezone.utc) - timedelta(hours=24)
    data = json.loads(_STATE_FILE.read_text())
    return datetime.fromisoformat(data["last_scan_at"])


def save_last_scan_at(dt: datetime) -> None:
    data = {}
    if _STATE_FILE.exists():
        data = json.loads(_STATE_FILE.read_text())
    data["last_scan_at"] = dt.isoformat()
    _STATE_FILE.write_text(json.dumps(data, indent=2))
