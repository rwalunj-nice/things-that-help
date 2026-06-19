from unittest.mock import MagicMock, patch
from models import Bug
from scan import should_skip, run_scan


def _make_bug(key="INT-001", labels=None, resolution=None, priority="P1"):
    return Bug(
        key=key, summary="Test bug", description="Desc",
        priority=priority, labels=labels or [],
        assignee_name="Alice", assignee_account_id="acc",
        resolution=resolution,
    )


def test_skip_clone_label():
    bug = _make_bug(labels=["CLONE", "INT_CFB"])
    assert should_skip(bug) == ("clone", "CLONE label present")


def test_skip_cicd_label():
    bug = _make_bug(labels=["CICD_FAIL_BUG"])
    assert should_skip(bug) == ("cicd", "CICD_FAIL_BUG label present")


def test_skip_duplicate_resolution():
    bug = _make_bug(resolution="Duplicate")
    assert should_skip(bug) == ("duplicate", "resolution is Duplicate")


def test_no_skip_for_normal_bug():
    bug = _make_bug(labels=["INT_CFB"], resolution=None)
    assert should_skip(bug) is None


def test_no_skip_for_unset_priority():
    bug = _make_bug(priority="Unset", labels=[])
    assert should_skip(bug) is None


def test_run_scan_skips_clone_bug(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    clone_bug = _make_bug(labels=["CLONE"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [clone_bug]
    mock_claude = MagicMock()

    run_scan(mock_jira, mock_claude, filter_id="101489", label="INT_RCA_CANDIDATE", dry_run=False)

    mock_claude.judge_rca_eligibility.assert_not_called()
    mock_jira.add_label.assert_not_called()


def test_run_scan_adds_label_for_eligible_bug(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bug = _make_bug(labels=["INT_CFB"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [bug]
    mock_claude = MagicMock()
    mock_claude.judge_rca_eligibility.return_value = {
        "eligible": True, "reason": "Service outage", "confidence": "high"
    }

    run_scan(mock_jira, mock_claude, filter_id="101489", label="INT_RCA_CANDIDATE", dry_run=False)

    mock_jira.add_label.assert_called_once_with("INT-001", "INT_RCA_CANDIDATE")


def test_run_scan_dry_run_does_not_add_label(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bug = _make_bug(labels=["INT_CFB"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [bug]
    mock_claude = MagicMock()
    mock_claude.judge_rca_eligibility.return_value = {
        "eligible": True, "reason": "Outage", "confidence": "high"
    }

    run_scan(mock_jira, mock_claude, filter_id="101489", label="INT_RCA_CANDIDATE", dry_run=True)

    mock_jira.add_label.assert_not_called()


def test_run_scan_updates_state(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = []
    mock_claude = MagicMock()

    run_scan(mock_jira, mock_claude, filter_id="101489", label="INT_RCA_CANDIDATE", dry_run=False)

    state_file = tmp_path / "state.json"
    assert state_file.exists()
