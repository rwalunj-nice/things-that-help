import json
from unittest.mock import patch, MagicMock
from claude_client import ClaudeClient


def _mock_claude_response(text: str):
    mock_msg = MagicMock()
    mock_msg.content = [MagicMock(text=text)]
    return mock_msg


def test_judge_eligibility_returns_eligible_true():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": True, "reason": "Service outage", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.judge_rca_eligibility(
            summary="DB sync failed causing outage",
            description="Multiple services went down",
            priority="P1",
            labels=["INT_CFB"],
        )

    assert result["eligible"] is True
    assert result["confidence"] == "high"


def test_judge_eligibility_returns_eligible_false():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": False, "reason": "Trivial typo fix", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.judge_rca_eligibility(
            summary="Fix typo in error message",
            description="Changed 'occured' to 'occurred'",
            priority="P3",
            labels=[],
        )

    assert result["eligible"] is False


def test_analyze_rca_gaps_returns_structured_output():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({
        "rubric_gaps": ["'How was it missed?' is too generic"],
        "five_whys_chain": [
            {"why": "DB left in partial state", "covered": True, "note": ""},
            {"why": "DDL broke transaction", "covered": True, "note": ""},
            {"why": "No DB review checklist", "covered": False, "note": "Not addressed"},
        ],
        "deepest_unanswered_why": "No MySQL DDL standards exist in review process",
        "comment_markdown": "🤖 RCA Bot Review\n\nRUBRIC GAPS:\n..."
    })

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.analyze_rca_gaps(
            rca_text="What happened: DB sync failed...",
            fix_text="Changed DDL to use SET FOREIGN_KEY_CHECKS...",
            bug_summary="WFM Config: Make Sync Atomic Again",
            bug_description="Sync process lost transactional atomicity",
        )

    assert len(result["rubric_gaps"]) == 1
    assert len(result["five_whys_chain"]) == 3
    assert result["five_whys_chain"][2]["covered"] is False
    assert "comment_markdown" in result


def test_analyze_rca_uses_sonnet_model():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({
        "rubric_gaps": [], "five_whys_chain": [],
        "deepest_unanswered_why": "", "comment_markdown": "ok"
    })

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)) as mock_create:
        client.analyze_rca_gaps("rca", "fix", "summary", "desc")

    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == "claude-sonnet-4-6"


def test_judge_eligibility_uses_haiku_model():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": True, "reason": "test", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)) as mock_create:
        client.judge_rca_eligibility("summary", "desc", "P1", [])

    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == "claude-haiku-4-5-20251001"
