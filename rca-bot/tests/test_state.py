import json
from datetime import datetime, timezone
from pathlib import Path
import pytest
from state import load_last_scan_at, save_last_scan_at


def test_load_returns_24h_ago_when_no_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = load_last_scan_at()
    now = datetime.now(timezone.utc)
    diff = (now - result).total_seconds()
    assert 86300 < diff < 86500  # ~24 hours


def test_save_and_load_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    dt = datetime(2026, 6, 20, 9, 0, 0, tzinfo=timezone.utc)
    save_last_scan_at(dt)
    loaded = load_last_scan_at()
    assert loaded == dt
