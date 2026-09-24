# 04 · Blog articles (source of truth)

These 20 Markdown files are the **only** place articles are edited. The website (`03_Website`) copies them in at build time.

**Status: all 20 are `ready-for-review`. None is published.** A production build includes only articles whose status is `approved` or `published` (see the approval gate below).

## Index

| # | Title | Slug | Category | Review type | Sources | Words (excl. prompt blocks) | Status |
|---|---|---|---|---|---|---|---|
| 1 | How to Write a Proposal with AI That Doesn't Sound Generic | `write-a-proposal-with-ai` | Client Workflows | guide | 2 | 855 | ready-for-review |
| 2 | Scope Creep Emails: Four Templates That Protect the Relationship | `scope-creep-email-templates` | Client Workflows | guide | 1 | 565 | ready-for-review |
| 3 | The Client Onboarding Checklist for Freelancers (Run It in 30 Minutes) | `client-onboarding-checklist` | Client Workflows | guide | 2 | 1,019 | ready-for-review |
| 4 | The Five-Minute Weekly Client Update (Template + AI Prompt) | `weekly-client-update-template` | Client Workflows | guide | 1 | 627 | ready-for-review |
| 5 | A Payment Reminder Schedule for Freelancers: Five Stages, Five Templates | `payment-reminder-schedule` | Getting Paid | guide | 2 | 662 | ready-for-review |
| 6 | Deposits, Milestones and Payment Terms: What to Put in Writing Before You Start | `deposits-and-payment-terms` | Getting Paid | guide | 2 | 861 | ready-for-review |
| 7 | How to Track Invoices and Payment Reminders in Google Sheets or Excel (Tested Formulas) | `track-invoices-in-a-spreadsheet` | Getting Paid | tested | 1 | 908 | ready-for-review |
| 8 | What to Include on Every Invoice: A Checklist for Freelancers | `what-to-include-on-an-invoice` | Getting Paid | guide | 2 | 765 | ready-for-review |
| 9 | 12 AI Prompts for Client Emails (With Inputs and Guardrails) | `ai-prompts-for-client-emails` | AI, Done Right | guide | 2 | 327 | ready-for-review |
| 10 | How to Keep Client Data Private When You Use ChatGPT, Claude or Gemini | `client-data-privacy-ai` | AI, Done Right | researched | 6 | 951 | ready-for-review |
| 11 | How to Make AI Drafts Sound Like You (the Voice Profile Method) | `make-ai-sound-like-you` | AI, Done Right | guide | 2 | 668 | ready-for-review |
| 12 | The AI Business Brief: One Page of Context That Improves Every Prompt | `ai-business-brief` | AI, Done Right | guide | 2 | 718 | ready-for-review |
| 13 | How to Write SOPs for a One-Person Business (Template + AI Prompt) | `sop-template-one-person-business` | Systems & SOPs | guide | 1 | 575 | ready-for-review |
| 14 | The Minimum Tool Stack for a Solo Service Business | `minimum-tool-stack` | Systems & SOPs | researched | 7 | 839 | ready-for-review |
| 15 | The Weekly Admin Review: A 45-Minute Agenda That Keeps Everything Moving | `weekly-admin-review` | Systems & SOPs | guide | 2 | 763 | ready-for-review |
| 16 | What to Automate First: A Simple Scoring Method for Solo Businesses | `what-to-automate-first` | Systems & SOPs | guide | 3 | 907 | ready-for-review |
| 17 | MailerLite vs Kit vs beehiiv for a Service Business Newsletter | `mailerlite-vs-kit-vs-beehiiv` | Tools, Honestly | researched | 4 | 871 | ready-for-review |
| 18 | Make vs Zapier vs n8n for Freelancers: Which Automation Tool Fits? | `make-vs-zapier-vs-n8n` | Tools, Honestly | researched | 3 | 866 | ready-for-review |
| 19 | Spreadsheet, Notion or CRM: Where Should a Solo Business Track Clients? | `spreadsheet-vs-notion-vs-crm` | Tools, Honestly | researched | 2 | 714 | ready-for-review |
| 20 | Tally vs Google Forms vs Jotform for Client Intake Forms | `client-intake-form-tools` | Tools, Honestly | researched | 3 | 742 | ready-for-review |

Review types: **guide** = method/how-to article; **tested** = we ran it ourselves (method stated in `tested_note`); **researched** = based on official documentation and pricing pages checked on the stated date, not hands-on tested.

## Front matter schema

```yaml
title: "…"                 # H1 and <title>
description: "…"           # meta description, 110–158 characters
slug: kebab-case           # URL: /blog/<slug>/
category: client-workflows | getting-paid | ai-done-right | systems-sops | tools-honestly
date: 2026-09-24           # first published (or drafted)
updated: 2026-09-24        # last factual review
review_type: guide | tested | researched
tested_note: "…"           # required for tested/researched: how and when
status: draft | ready-for-review | approved | published | rejected | archived
tags: [ … ]
product_cta: starter | playbook | desk | prompts | bundle
related: [slug, slug, slug]
download: /downloads/…     # optional
affiliate: true            # ONLY if the article contains issued affiliate links (adds the disclosure box)
sources:
  - title: "…"
    url: "https://…"
    accessed: 2026-09-24
```

## Approval gate (how an article goes live)

1. Writer/automation creates the file with `status: draft`.
2. QA passes (`python3 Content_Automation_Business/08_Automation_Workflows/scripts/qa_check.py <file>`) → `status: ready-for-review`.
3. **You** read it and change the status to `approved` (or `rejected` with a note), usually by approving the pull request the pipeline opens.
4. The next production build (`npm run build` in `03_Website`) includes it. Once it's live, set `status: published`.

## Editorial rules (summary)

- Every factual claim or statistic has a source listed in `sources`, with the date checked.
- Examples are fictional and labeled as such. No invented testimonials, results, quotes or experiences.
- Tool prices and limits say "checked [date]" and link to the official page.
- No affiliate links unless the program has issued them to you. Then set `affiliate: true` and label each link.
- Legal, tax and financial topics are framed as general information with a "check locally" note.

Full policy: `03_Website/src/editorial-policy.md` · QA checklist: `08_Automation_Workflows/`.
