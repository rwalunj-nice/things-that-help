from unittest.mock import MagicMock, call
from models import Bug
from review import run_review


def _make_bug(key="INT-001", rca_text="", fix_text="", summary="Test bug", description="Desc"):
    return Bug(
        key=key, summary=summary, description=description,
        priority="P1", labels=[],
        assignee_name="Alice", assignee_account_id="acc",
        resolution=None, rca_text=rca_text, fix_text=fix_text,
    )


def test_skip_already_reviewed():
    bug = _make_bug(rca_text="Some RCA")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = True
    mock_claude = MagicMock()

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_not_called()
    mock_jira.post_comment.assert_not_called()


def test_empty_rca_posts_placeholder():
    bug = _make_bug(rca_text="")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = False
    mock_claude = MagicMock()

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_not_called()
    mock_jira.post_comment.assert_called_once_with(
        "INT-001", "RCA content not yet filled in — nothing to review yet."
    )


def test_whitespace_only_rca_posts_placeholder():
    bug = _make_bug(rca_text="   \n  ")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = False
    mock_claude = MagicMock()

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_jira.post_comment.assert_called_once_with(
        "INT-001", "RCA content not yet filled in — nothing to review yet."
    )


def test_posts_review_comment_for_filled_rca():
    bug = _make_bug(rca_text="Root cause was X", fix_text="Fixed by Y")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = False
    mock_claude = MagicMock()
    mock_claude.analyze_rca_gaps.return_value = {
        "rubric_gaps": ["Missing prevention actions"],
        "five_whys_chain": [],
        "deepest_unanswered_why": "No standards exist",
        "comment_markdown": "## RCA Review\n\nGaps found.",
    }

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_called_once_with(
        rca_text="Root cause was X",
        fix_text="Fixed by Y",
        bug_summary="Test bug",
        bug_description="Desc",
    )
    mock_jira.post_comment.assert_called_once_with("INT-001", "## RCA Review\n\nGaps found.")


def test_claude_error_does_not_abort_loop():
    bug1 = _make_bug(key="INT-001", rca_text="RCA content")
    bug2 = _make_bug(key="INT-002", rca_text="More RCA content")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug1, bug2]
    mock_jira.has_bot_comment.return_value = False
    mock_claude = MagicMock()
    mock_claude.analyze_rca_gaps.side_effect = [Exception("Claude error"), {
        "rubric_gaps": [],
        "five_whys_chain": [],
        "deepest_unanswered_why": "",
        "comment_markdown": "Review OK",
    }]

    run_review(mock_jira, mock_claude, filter_id="97314")

    # INT-001 failed but INT-002 should still be processed
    mock_jira.post_comment.assert_called_once_with("INT-002", "Review OK")


def test_jira_error_does_not_abort_loop():
    bug1 = _make_bug(key="INT-001", rca_text="RCA content")
    bug2 = _make_bug(key="INT-002", rca_text="More RCA content")
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = [bug1, bug2]
    mock_jira.has_bot_comment.side_effect = [Exception("Jira error"), False]
    mock_claude = MagicMock()
    mock_claude.analyze_rca_gaps.return_value = {
        "rubric_gaps": [], "five_whys_chain": [],
        "deepest_unanswered_why": "", "comment_markdown": "Review OK",
    }

    run_review(mock_jira, mock_claude, filter_id="97314")

    # INT-001 failed on has_bot_comment but INT-002 should still be processed
    mock_jira.post_comment.assert_called_once_with("INT-002", "Review OK")


def test_multiple_bugs_processed_independently():
    bugs = [
        _make_bug(key="INT-001", rca_text="RCA 1"),
        _make_bug(key="INT-002", rca_text=""),
        _make_bug(key="INT-003", rca_text="RCA 3"),
    ]
    mock_jira = MagicMock()
    mock_jira.get_filter_bugs.return_value = bugs
    mock_jira.has_bot_comment.return_value = False
    mock_claude = MagicMock()
    mock_claude.analyze_rca_gaps.return_value = {
        "rubric_gaps": [], "five_whys_chain": [],
        "deepest_unanswered_why": "", "comment_markdown": "OK",
    }

    run_review(mock_jira, mock_claude, filter_id="97314")

    assert mock_claude.analyze_rca_gaps.call_count == 2  # INT-001 and INT-003
    assert mock_jira.post_comment.call_count == 3  # 2 reviews + 1 placeholder
