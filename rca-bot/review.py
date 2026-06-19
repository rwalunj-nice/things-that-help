import logging
from config import load_config
from jira_client import JiraClient
from claude_client import ClaudeClient
from models import Bug

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

_EMPTY_RCA_COMMENT = "RCA content not yet filled in — nothing to review yet."


def run_review(jira: JiraClient, claude: ClaudeClient, filter_id: str) -> None:
    bugs = jira.get_filter_bugs(filter_id)
    log.info(f"Reviewing {len(bugs)} bugs from filter {filter_id}")

    for bug in bugs:
        try:
            if jira.has_bot_comment(bug.key):
                log.info(f"[{bug.key}] already reviewed — skipping")
                continue

            if not bug.rca_text.strip():
                jira.post_comment(bug.key, _EMPTY_RCA_COMMENT)
                log.info(f"[{bug.key}] no RCA content — posted placeholder")
                continue

            result = claude.analyze_rca_gaps(
                rca_text=bug.rca_text,
                fix_text=bug.fix_text,
                bug_summary=bug.summary,
                bug_description=bug.description,
            )
            jira.post_comment(bug.key, result["comment_markdown"])
            log.info(f"[{bug.key}] review comment posted")
        except Exception as exc:
            log.error(f"[{bug.key}] review failed: {exc}")


if __name__ == "__main__":
    cfg = load_config()
    jira = JiraClient(cfg)
    claude = ClaudeClient(cfg.anthropic_api_key)
    run_review(jira, claude, filter_id=cfg.jira_filter_rca_flagged)
