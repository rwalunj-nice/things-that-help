from unittest.mock import MagicMock
from models import Bug
from remind import run_reminder


def _make_bug(key="INT-001", summary="Test bug", assignee_name="Alice"):
    return Bug(
        key=key, summary=summary, description="",
        priority="P1", labels=[],
        assignee_name=assignee_name, assignee_account_id="acc",
        resolution=None,
    )


def test_run_reminder_posts_bugs():
    bugs = [_make_bug("INT-001"), _make_bug("INT-002")]
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = bugs
    mock_teams = MagicMock()

    run_reminder(mock_jira, mock_teams, filter_id="97314")

    mock_jira.get_filter_bugs.assert_called_once_with("97314")
    mock_teams.post_reminder.assert_called_once_with(bugs)


def test_run_reminder_empty_filter():
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = []
    mock_teams = MagicMock()

    run_reminder(mock_jira, mock_teams, filter_id="97314")

    mock_teams.post_reminder.assert_called_once_with([])


def test_run_reminder_uses_filter_id():
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = []
    mock_teams = MagicMock()

    run_reminder(mock_jira, mock_teams, filter_id="12345")

    mock_jira.get_filter_bugs.assert_called_once_with("12345")
