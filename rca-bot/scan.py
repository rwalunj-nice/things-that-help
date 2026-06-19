import argparse
import logging
from datetime import datetime, timezone
from config import load_config
from jira_client import JiraClient
from claude_client import ClaudeClient
from models import Bug
from state import load_last_scan_at, save_last_scan_at

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


_SKIP_LABELS = {
    "CLONE": ("clone", "CLONE label present"),
    "CICD_FAIL_BUG": ("cicd", "CICD_FAIL_BUG label present"),
}


def should_skip(bug: Bug) -> tuple | None:
    for label in bug.labels:
        if label in _SKIP_LABELS:
            return _SKIP_LABELS[label]
    if bug.resolution == "Duplicate":
        return ("duplicate", "resolution is Duplicate")
    return None


def run_scan(jira: JiraClient, claude: ClaudeClient, filter_id: str, label: str, dry_run: bool = False) -> None:
    since = load_last_scan_at()
    log.info(f"Scanning bugs since {since.isoformat()}")
    if dry_run:
        log.info("dry_run=True — no labels will be written")

    bugs = jira.get_bugs_since(filter_id, since)
    log.info(f"Found {len(bugs)} new bugs")

    for bug in bugs:
        skip = should_skip(bug)
        if skip:
            log.info(f"SKIP [{bug.key}] reason={skip[0]}: {skip[1]}")
            continue

        try:
            result = claude.judge_rca_eligibility(
                summary=bug.summary,
                description=bug.description,
                priority=bug.priority,
                labels=bug.labels,
            )
        except Exception as exc:
            log.error(f"[{bug.key}] Claude call failed, skipping: {exc}")
            continue
        log.info(
            f"[{bug.key}] eligible={result['eligible']} "
            f"confidence={result['confidence']} reason={result['reason']}"
        )

        if result["eligible"] and not dry_run:
            try:
                jira.add_label(bug.key, label)
                log.info(f"[{bug.key}] labeled {label}")
            except Exception as exc:
                log.error(f"[{bug.key}] failed to add label: {exc}")

    save_last_scan_at(datetime.now(timezone.utc))
    log.info("Scan complete. State updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily RCA eligibility scan")
    parser.add_argument("--dry-run", action="store_true", help="Do not write labels to Jira")
    args = parser.parse_args()

    cfg = load_config()
    jira = JiraClient(cfg)
    claude = ClaudeClient(cfg.anthropic_api_key)

    run_scan(jira, claude, filter_id=cfg.jira_filter_screening, label=cfg.jira_label_rca_candidate, dry_run=args.dry_run)
