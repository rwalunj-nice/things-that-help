from unittest.mock import patch, MagicMock
from models import Bug
from teams_client import TeamsClient


def _make_bug(key, summary, assignee):
    return Bug(
        key=key, summary=summary, description="", priority="P1",
        labels=[], assignee_name=assignee, assignee_account_id="acc",
        resolution=None,
    )


def test_post_reminder_calls_webhook():
    client = TeamsClient("https://webhook.example.com")
    bugs = [_make_bug("INT-001", "DB outage", "Alice")]
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder(bugs)

    mock_post.assert_called_once()
    url = mock_post.call_args.args[0]
    assert url == "https://webhook.example.com"


def test_post_reminder_includes_all_bug_keys():
    client = TeamsClient("https://webhook.example.com")
    bugs = [
        _make_bug("INT-001", "Bug one", "Alice"),
        _make_bug("INT-002", "Bug two", "Bob"),
    ]
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder(bugs)

    body = mock_post.call_args.kwargs["json"]
    text = body["text"]
    assert "INT-001" in text
    assert "INT-002" in text
    assert "Alice" in text
    assert "Bob" in text


def test_post_reminder_with_empty_list_still_posts():
    client = TeamsClient("https://webhook.example.com")
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder([])

    mock_post.assert_called_once()
