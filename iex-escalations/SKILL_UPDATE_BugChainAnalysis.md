# IEX Escalation Analysis Skill - Bug Chain Analysis Enhancement

## Purpose
This document contains the critical enhancement to the `iex-escalation-analysis` skill to ensure complete bug dependency chain analysis in all future scheduled task executions.

## Location to Update
File: `/sessions/serene-modest-pasteur/mnt/.claude/skills/iex-escalation-analysis/SKILL.md`

Section: After "Check 2 — Bug References in Comments" (around line 148-156)

## New Content to Insert

Add the following section as **Check 3** before the "Fix Version & Bug Analysis — Report Sub-section":

---

**Check 3 — CRITICAL: Follow the Complete Bug Dependency Chain:**

**MANDATORY:** After identifying the primary bug(s) via "is fixed by" or comment references, you MUST check if those bugs have additional related bugs via "relates to", "blocks", "is blocked by", "depends on", or similar relationship types. Bug fixes often have dependencies or related context in other tickets that are essential for complete root cause understanding.

**Why This Matters:** A bug may appear to be "in progress" for the primary issue, but a related bug might already be DONE with a partial fix deployed. Missing this chain means missing critical context about what's already fixed vs. what's still pending.

**Process:**
1. For each bug found in Check 1 or Check 2, examine its `issuelinks` field
2. Look for relationship types including (but not limited to):
   - "relates to" — often contains foundational bugs or related context
   - "blocks" / "is blocked by" — dependency chain
   - "depends on" / "is depended on by" — prerequisite fixes
   - "clones" / "is cloned by" — version-specific instances (usually skip clones unless they add context)
3. For each non-clone related bug found, fetch that ticket: `Atlassian:getJiraIssue(issueId=<related-bug-id>)`
4. Extract the same fields as Check 1 (summary, status, fix version, components, root cause)
5. Determine the relationship and impact:
   - If related bug is DONE: check if it provides partial mitigation or prerequisite fix
   - If related bug is In Progress: check if it's blocking the primary bug
   - Document the dependency chain clearly in the report

**Example Scenario (Real Case from June 11, 2026 Report):**
- Escalation WFM-176982 (Assurant Inc) → "is fixed by" → Bug WFM-173234 (Status: New, 8.1.Future - Integration issue)
- Bug WFM-173234 → "relates to" → Bug WFM-173231 (Status: DONE, 8.1.5 - Query safety net)
- **Complete Picture:** 
  - WFM-173231 (DONE in 8.1.5): Query modified to use r_agtsysstats instead of r_agtqueuestats, providing immediate mitigation by avoiding corrupt data
  - WFM-173234 (In Progress, 8.1.Future): Root cause investigation—why SWXIFACE inserts invalid r_agtqueuestats records
  - **Two-Tier Fix:** Partial mitigation already deployed (8.1.5), complete fix pending (8.1.Future)
- **Without Check 3:** Report would miss that customers on 8.1.5+ are already protected by query safety net, giving incomplete and potentially misleading status

**CRITICAL:** Do NOT stop at the first bug. Always traverse the full dependency graph (excluding clones unless they add unique context) to get complete fix version and root cause picture.

**Report Format for Bug Chains:**
When a bug has related dependencies, structure the Fix Version & Bug Analysis section to show the complete chain:

```
Fix Version & Bug Analysis

PRIMARY BUG (Integration Issue):
Bug: WFM-173234 – Unexpected r_agtqueuestats records for unassigned queues
Status: New
Priority: P2
Fix Version(s): 8.1.Future
Source: Linked via 'is fixed by' relationship
Root Cause: SWXIFACE inserting invalid records—investigation in progress
Components Affected: SWXIFACE, r_agtqueuestats table

RELATED BUG (Query Safety Net - ALREADY FIXED):
Bug: WFM-173231 – Estimated Staff value mismatch in MU Results exporter
Status: Done (SVN r188387)
Priority: P2
Fix Version(s): 8.1.5
Source: WFM-173234 'relates to' WFM-173231
Root Cause: Query incorrectly keyed off r_agtqueuestats instead of r_agtsysstats
Fix Applied: Query modified to use authoritative data source, bypassing corrupt records
Components Affected: SmartSync, MU Results exporter

TWO-TIER FIX STRATEGY:
Tier 1 (Mitigation - DEPLOYED): Query modification in 8.1.5 provides safety net
Tier 2 (Root Cause - IN PROGRESS): Integration fix in 8.1.Future prevents invalid data
```

---

## Quality Checklist Update

Add to the existing Quality Checklist (around line 298):

☐ **Complete bug dependency chain analyzed** (Check 1, 2, AND 3 performed)
☐ **Related bugs via "relates to", "blocks", "depends on" examined and fetched**
☐ **Multi-tier fix strategies identified** (partial fixes vs. complete fixes)
☐ **Bug chain dependencies clearly documented in report** (PRIMARY + RELATED structure)

---

## Implementation Notes

This enhancement ensures that future automated weekly reports will:
1. Never miss partial fixes that are already deployed
2. Clearly communicate multi-tier fix strategies to leadership
3. Provide complete engineering context by following the full bug dependency graph
4. Avoid misleading status reports that only show "in progress" primary bugs while missing "done" related mitigations

The June 11, 2026 report on WFM-176982 (Assurant Inc) has been corrected using this approach and serves as the reference implementation.

---

## Action Required

1. Copy the "Check 3" section above into the SKILL.md file after "Check 2"
2. Add the Quality Checklist items to the existing checklist section
3. Test the next scheduled execution to verify the enhanced analysis is applied
4. File this document in the IEX Escalations reference folder for future skill maintenance
