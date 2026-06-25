---
name: iex-escalation-analysis
description: Generate engineering-actionable escalation reports for IEX WFM customer issues. Use this skill whenever the user asks to analyze IEX escalations, create escalation reports, generate status updates on customer escalations, summarize escalation boards, review escalation tickets, or prepare escalation summaries for leadership. Also trigger when user mentions Jira escalation boards, WFM escalations, customer escalations requiring detailed analysis, or any request involving analyzing multiple customer issues from Jira/Atlassian. The skill fetches data from Atlassian/Jira, analyzes each escalation in depth, and produces comprehensive reports with root cause findings, technical details, fix targets, and actionable next steps.
---

# IEX Escalation Analysis

This skill generates engineering-actionable escalation reports for IEX WFM (Workforce Management) customer issues by analyzing Jira tickets and producing detailed status reports that include root cause findings, technical details, fix targets, and next steps.

## When to Use This Skill

Trigger this skill when the user:
- Asks to analyze IEX escalations or customer escalations
- Requests an escalation report or status summary
- Wants to review escalation tickets from a Jira board
- Mentions analyzing customer issues from Atlassian/Jira
- Needs a summary of active escalations for leadership
- References a Jira Structure board URL
- Wants detailed status on WFM escalations

## Chrome vs. API Usage Rules

**CRITICAL - Use Chrome ONLY for:**
- Structure board URLs (cannot be accessed via API)
- Taking screenshots of board views

**ALWAYS Use Atlassian API for:**
- Individual Jira ticket data (WFM-174707, WFM-173128, etc.)
- Fetching issue details, descriptions, comments, status
- All ticket information retrieval

**Workflow:**
1. Structure board URL → Use Chrome to screenshot → Extract ticket IDs
2. Ticket IDs → Use Atlassian API to fetch details
3. NEVER use Chrome to access individual ticket URLs unless API fails

## Core Principle: Findings Reporting, Not Activity Reporting

**CRITICAL**: This skill generates reports that are **engineering-actionable**, not just status-tracking. The key principle is:

> **Shift from "activity reporting" (we collected logs, we analyzed) to "findings reporting" (we discovered X, root cause is Y, fix will go in Z component/version).**

Reports must answer:
- ✅ Where does the fix need to go? (Component, version)
- ✅ What did we actually discover? (Root cause, not just "we investigated")
- ✅ What's the technical nature? (Defect vs. config vs. external vendor issue)
- ✅ What interim actions were taken? (Workarounds, recommendations)
- ✅ What's the collaboration context? (Weekly calls, vendor dependencies)

## Workflow

### Step 1: Gather Escalation Data

**From Jira Structure Board URL:**
When user provides a Structure board URL (e.g., `https://nice-ce-cxone-prod.atlassian.net/jira/apps/.../structure/board/8417`):

1. **Use Chrome to Access and Screenshot:**
   - Load the necessary Chrome tools: `tool_search(query="Chrome browser screenshot")`
   - Get tab context: `Claude in Chrome:tabs_context_mcp(createIfEmpty=true)`
   - Navigate to the Structure board URL: `Claude in Chrome:navigate(tabId=X, url=<structure_board_url>)`
   - Wait for page to load: 3-5 seconds
   - Take screenshot: `Claude in Chrome:computer(action="screenshot", tabId=X)`
   - If content not visible, scroll down and take another screenshot

2. **Extract Ticket IDs from Screenshot:**
   - Analyze the screenshot to identify all visible ticket IDs (e.g., WFM-174707, WFM-173128, WFM-173223)
   - Look for the standard Jira ticket format: PROJECT-NUMBER (e.g., WFM-XXXXX)
   - Create a list of all identified tickets

3. **Fetch Each Ticket Using Atlassian API:**
   - For each ticket ID, call `Atlassian:getJiraIssue` to retrieve full details
   - NEVER use Chrome to access individual ticket URLs - always use the API
   - API provides complete structured data faster and more reliably

**From Screenshot Uploaded by User:**
1. If user provides a screenshot of escalations, extract the ticket IDs (e.g., WFM-174707, WFM-173128)
2. Fetch each ticket using Atlassian API

**From List of Ticket IDs:**
1. If user provides a list of ticket IDs, use those directly
2. Fetch each ticket using Atlassian API

**Fetching Each Escalation (Always Use API):**
For each ticket ID, call `Atlassian:getJiraIssue` to retrieve:
- Summary (title)
- Description (problem details)
- Status (In Progress, Pending Support, Open)
- Assignee
- Issue type
- Any custom fields that contain technical details
- Comments (for additional investigation findings)

### Step 2: Analyze Each Escalation

For each escalation, extract and organize:

**A. Basic Information**
- Ticket ID
- Customer name
- Current status
- Assignee

**B. Technical Classification**
From the description and any investigation notes, identify:
- **Component/System**: SWIFACE, SWXEVD, HRdirect, RTA Gateway, Connection Manager, etc.
- **Issue Type**: Possible Defect, Bug, Configuration Issue, External Vendor Issue
- **Fix Target** (if known): Version numbers (8.1.5, 8.2, 8.0.9)
- **Root Cause** (if identified): Specific technical finding

**C. Investigation Findings**
Look for and extract:
- Root cause analysis
- Technical details (APIs, database tables, code paths affected)
- Architectural context (configuration specifics, deployment topology)
- External dependencies (vendor involvement, third-party systems)
- Workarounds provided to customer

**D. Collaboration Context**
- Vendor coordination (weekly calls, escalation to other teams)
- Internal escalations (Richardson team, R&D involvement)
- Communication cadence

### Step 3: Generate the Report

Create a comprehensive Word document with the following structure:

#### Report Header
```
Title: IEX Escalations - Detailed Status Report
Subtitle: Report Date: [Current Date]
```

#### Executive Summary
- Total number of escalations
- High-level categorization (RTA issues, integrations, data quality, etc.)
- Critical callouts (unassigned, customer trust issues)
- Status distribution table

#### Individual Escalation Sections

For each escalation, use this **enhanced format**:

**Title Format:**
```
[Ticket ID] - [Customer Name] – [Fix Status/Component/Classification]
```

Examples:
- `WFM-174707 - CALNG EDD UI – Bug fixed in 8.2 now being ported to 8.1.x = 8.1.5`
- `WFM-173223 - United Health Group – Issue at LivePerson ACD end who is working on the fix`
- `WFM-174996 - SaskEnergy – SWIFACE issue on historical side`
- `WFM-175030 - Discover Financial – Possible defect fix`

**Section Content:**

**Description:** 
Clear technical problem statement with customer impact, affected systems/versions, and frequency patterns.

**Current Status:** 
`[Status Flag] | Assignee: [Name]`

**Work Done:** 
⚠️ **MOST CRITICAL SECTION** - Report FINDINGS, not just activities.

Must include:
1. **Root Cause Findings** - What was discovered during investigation
2. **Technical Details** - Specific components, APIs, database tables involved
3. **Architectural Context** - Configuration specifics, system topology
4. **Vendor/External Dependencies** - Third-party involvement
5. **Workarounds Provided** - Interim solutions given to customer

✓ **Good Example:**
"Issue reproduced. Root cause identified: LivePerson ACD is calling agent state API even after token expiration. They need to implement token refreshment mechanism. UHG vendor managing partner confirmed. Weekly sync call established every Tuesday."

✗ **Bad Example:**
"Issue reproduced. Logs collected. Investigation ongoing."

**Next Steps:**
Specific, actionable items for resolution. Must be clear enough that another engineer could pick up the work.

#### Critical Actions Required
Bulleted list of urgent items with priority flags:
- **URGENT:** Items requiring immediate action (unassigned tickets, production issues)
- **HIGH PRIORITY:** Customer trust issues, data accuracy problems
- Regular priority items

### Step 4: Present the Report

Save the report as a Word document with filename format:
`IEX_Escalations_Detailed_Report_[Date].docx`

Present the file to the user with a brief summary highlighting:
- Total escalation count
- Critical/urgent items requiring immediate attention
- Key themes or patterns identified

## Enhanced Content Requirements

### Title Enhancement
Always add fix status/component/classification to the title when available:

**Component Examples:**
- SWIFACE issue on historical side
- SWXEVD duplicate entries
- RTA Gateway failover
- HRdirect wait list processing

**Fix Status Examples:**
- Bug fixed in 8.2 now being ported to 8.1.x = 8.1.5
- Bug targeted with 8.0.x = 8.0.9, 8.1.5, 8.2
- Possible defect fix
- Possible Defect

**External Status Examples:**
- Issue at LivePerson ACD end who is working on the fix
- AWS integration issue
- WorkDay sync problem

### Work Done Enhancement

Transform basic investigation notes into findings-rich content:

**Pattern 1: External Vendor Issues**
- Identify the vendor and their role
- State the specific technical problem
- Note what they need to fix
- Include coordination details (weekly calls, escalation contacts)

Example: "LivePerson ACD is UHG vendor managing partner. They are calling agent state API even if token has expired. They need to implement token refreshment mechanism. Weekly call every Tuesday."

**Pattern 2: Architecture/Configuration Issues**
- Describe the unique environmental factor
- Explain how it contributes to the problem
- Provide recommendations

Example: "This is only customer where one CISCO ACD node is handling 15-20 channels. We have recommended setting up another node for load distribution."

**Pattern 3: Code/System Defects**
- Identify the specific component
- Explain the technical mechanism of the failure
- List all code paths or trigger points involved
- Suggest escalation path if needed

Example: "Possible Defect issue is on SWXEVD where duplicate entries going to DB. There are multiple trigger points using which this info can go into DB (webstation, RCP, smartsync, bulk schedule, individual schedule), need to review them in the code. It can possible go to Richardson team. DB dump asked for specific agents so that we identify trigger source."

**Pattern 4: Workarounds**
- Document the workaround clearly
- Note its reliability/limitations
- Explain what permanent fix is needed

Example: "Possible defect with date format in old plugin which is year end specific when input file is empty for SWIFACE issue. Workaround – KTR file change for date format. Internal defect to be created for permanent fix."

## Information to Extract from Jira

When analyzing tickets, actively look for:

**In Description Field:**
- Problem statement
- Customer impact
- System versions (WFM 8.1.2.0, Cisco ASC v1.4.0, etc.)
- Environmental details

**In Comments/Updates:**
- Root cause findings
- Investigation results
- Vendor communications
- Technical analysis
- Workarounds provided
- Coordination details

**From Custom Fields:**
- Component assignments
- Version targeting
- Priority/severity

## Quality Checks

Before finalizing the report, verify:

☐ Title includes fix status/component/classification (not just ticket + customer)
☐ Description includes customer impact and affected system versions
☐ Work Done reports FINDINGS, not just activities
☐ Root cause or suspected root cause is stated (if known)
☐ Technical details included (components, APIs, database tables, code paths)
☐ Workarounds documented (if any provided to customer)
☐ External vendor involvement noted (if applicable)
☐ Collaboration details included (weekly calls, escalation paths)
☐ Next Steps are specific and actionable
☐ URGENT/CRITICAL items are clearly flagged

## Output Format

Generate a professionally formatted Word document (.docx) with:
- US Letter page size (12240 x 15840 DXA)
- 0.5" margins (720 DXA)
- Arial font throughout
- Heading styles with consistent formatting
- Status distribution table
- Clear section breaks between escalations
- Bullet points for action items

## Common Pitfalls to Avoid

1. **Activity Logging Instead of Findings** - Don't just list what you did; report what you learned
2. **Generic Descriptions** - Be specific about the technical problem
3. **Missing Component Attribution** - Always identify which component has the issue
4. **No Fix Timeline** - Include target versions when known
5. **Vague Next Steps** - Be specific enough for handoff to another engineer
6. **Ignoring Workarounds** - Document all interim solutions provided
7. **Missing Collaboration Context** - Note vendor involvement and scheduled communications

## Reference Documents

For detailed formatting guidelines and examples, see:
- `references/template-guidelines.md` - Complete template with examples
- `references/example-report.md` - Annotated example of a good report

## Example Usage

**User Request:**
"Analyze the escalations from this Structure board: https://nice-ce-cxone-prod.atlassian.net/jira/apps/.../structure/board/8417"

**Skill Response:**
1. Load Chrome tools: `tool_search(query="Chrome browser screenshot")`
2. Connect to Chrome browser: `Claude in Chrome:select_browser` or `Claude in Chrome:switch_browser`
3. Create/get tab context: `Claude in Chrome:tabs_context_mcp(createIfEmpty=true)`
4. Navigate to Structure board: `Claude in Chrome:navigate(url=<structure_board_url>)`
5. Wait for page load: 3-5 seconds
6. Take screenshot: `Claude in Chrome:computer(action="screenshot")`
7. Extract ticket IDs from screenshot (e.g., WFM-174707, WFM-173128, WFM-173223...)
8. Fetch each ticket using Atlassian API: `Atlassian:getJiraIssue` for each ID
9. Analyze each ticket for findings, not just activities
10. Generate comprehensive Word document following the template
11. Present the report with executive summary

**User Request:**
"Analyze these escalations: WFM-174707, WFM-173128, WFM-175030"

**Skill Response:**
1. Fetch the three specified tickets using Atlassian API (skip Chrome entirely)
2. Extract all relevant information following the enhanced format
3. Generate detailed report with proper titles (including fix status)
4. Ensure Work Done sections report findings
5. Present final document

**User Request:**
"Here's a screenshot of the escalation board" [uploads image]

**Skill Response:**
1. Extract ticket IDs from the uploaded screenshot
2. Fetch each ticket using Atlassian API
3. Analyze and generate comprehensive report
4. Present final document

## Notes for Claude Using This Skill

- Always read the Jira tickets thoroughly, including all comments
- Look for technical details in comments, not just the description
- If information is sparse, note what's missing rather than inventing details
- When fix status is unknown, classify as "Investigation ongoing" or "Root cause analysis in progress"
- If multiple escalations have the same component issue, note this pattern in the executive summary
- For unassigned tickets, flag them prominently in the executive summary and action items

## Chrome Tool Requirements for Structure Boards

When accessing Structure board URLs, you need:
1. `tool_search(query="Chrome browser screenshot")` to load Chrome tools
2. `Claude in Chrome:tabs_context_mcp` to get/create tabs
3. `Claude in Chrome:navigate` to access the Structure board URL
4. `Claude in Chrome:computer` with action="screenshot" to capture the board
5. `Claude in Chrome:computer` with action="scroll" if board extends beyond viewport

**Important:**
- ONLY use Chrome for Structure board access and screenshots
- ALWAYS use Atlassian API (`Atlassian:getJiraIssue`) for individual ticket data
- If Chrome permission is denied, ask user to grant permission or provide screenshot manually
- After extracting ticket IDs from screenshot, immediately switch to API for all data fetching
