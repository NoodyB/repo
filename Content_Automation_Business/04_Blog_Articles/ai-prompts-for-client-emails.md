---
title: "12 AI Prompts for Client Emails (With Inputs and Guardrails)"
description: "Twelve copy-and-paste AI prompts for client emails, from new inquiries to invoices and testimonials, each with inputs and guardrails."
slug: ai-prompts-for-client-emails
category: ai-done-right
date: 2026-09-24
updated: 2026-09-24
review_type: guide
status: ready-for-review
tags: [AI prompts, client emails, templates]
product_cta: prompts
related: [ai-business-brief, make-ai-sound-like-you, client-data-privacy-ai]
sources:
  - title: "OpenAI Help Center, Prompt engineering best practices for ChatGPT"
    url: "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt"
    accessed: 2026-09-24
  - title: "Anthropic, Prompting best practices"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
    accessed: 2026-09-24
---

These twelve prompts cover the client emails that come up every week in a service business. Each one follows the same pattern: **clear inputs** in square brackets, a **defined output**, and **guardrails** that stop the assistant inventing prices, dates or promises.

They work in ChatGPT, Claude, Gemini and Copilot, including free plans. They'll work far better if you've created a [business brief](/blog/ai-business-brief/) and a [voice profile](/blog/make-ai-sound-like-you/) first. Several prompts ask for them.

**Before you paste anything:** replace client names and confidential details with placeholders. [Here's a quick privacy routine](/blog/client-data-privacy-ai/).

## Getting clients

### 1. Reply to a new inquiry

```text
Here is my business brief and voice profile: [PASTE]. A potential client sent this
inquiry (redacted): """[PASTE INQUIRY]""". Draft a reply under 150 words that: thanks
them and references one specific detail from their message; answers any direct
question they asked (if I haven't given you the answer, write [NEED INFO] instead of
guessing); asks the 2–3 most useful qualifying questions for my services; and ends
with my booking link [BOOKING LINK]. Match my voice profile. Don't mention prices
unless they asked and my brief includes them.
```

### 2. Follow up an inquiry that went quiet

```text
A potential client stopped replying [DAYS SINCE] days ago. Our last exchange:
"""[LAST MESSAGE SUMMARY]""". Write two alternative follow-up emails in my voice
[VOICE PROFILE], each under 90 words: Version A adds something useful (a relevant
tip, example or resource related to their project, without inventing facts about
them); Version B is a simple, friendly check-in that makes it easy to say "not now".
Neither should guilt-trip or imply urgency that doesn't exist. Include my booking
link [BOOKING LINK] once.
```

### 3. Discovery call follow-up

```text
Here are my rough notes from a discovery call (redacted): """[NOTES]""". Using my
voice profile [PASTE], write a follow-up email that: thanks them; summarizes their
goals, constraints and timeline in 3–5 bullets using their words where possible;
lists open questions; states the next step and date (e.g., "I'll send a proposal by
[DATE]"); and stays under 200 words. After the email, separately list anything in my
notes that is ambiguous or that I should clarify before writing a proposal.
```

### 4. Proposal follow-up sequence

```text
I sent a proposal for [PROJECT] on [DATE SENT]. Write three follow-up emails in my
voice [VOICE PROFILE]: Day 3 (one or two sentences: any questions?); Day 7 (offer a
15-minute call to walk through options, link [BOOKING LINK]); Day 14 (a gracious
close-the-loop message that assumes timing isn't right and leaves the door open).
Each under 80 words. No guilt, no fake deadlines.
```

For the proposal itself, see [how to write a proposal with AI that doesn't sound generic](/blog/write-a-proposal-with-ai/).

## During the project

### 5. Welcome email

```text
Using my business brief and voice profile [PASTE], write a welcome email for a new
client (redacted details: """[PROJECT, TIMELINE, LINKS]"""). Include: a warm opening
that references the project; a numbered "what happens next" list (agreement, deposit,
questionnaire link, kickoff booking link); my communication norms from the brief;
and a friendly close. Under 220 words. Use only the links and dates I provide. Use
[NEED INFO] for anything missing.
```

### 6. Weekly update from notes

```text
Turn my rough notes into a weekly client update using this structure: Done this week
/ Next week / Needed from you (with dates) / Risks or decisions. Notes (redacted):
"""[NOTES]""". Keep it under 150 words, in my voice [VOICE PROFILE]. If my notes
mention a delay, state it plainly with the new expected date. Don't soften it into
vagueness, and don't invent reasons.
```

More on the format: [the five-minute weekly client update](/blog/weekly-client-update-template/).

### 7. Delay notification

```text
Write an email telling a client that [MILESTONE] will move from [ORIGINAL DATE] to
[NEW DATE]. Reason (share appropriately): [REASON]. What I'm doing about it: [PLAN].
Structure: the news first, one sentence of context, the plan, the impact on later
milestones, and whether they need to do anything. Take responsibility where it's
mine, no excessive apology, under 150 words, in my voice [VOICE PROFILE].
```

### 8. Scope change request

```text
A client asked for something outside our agreed scope. Agreed scope: """[SCOPE]""".
Their request: """[REQUEST]""". Draft a friendly, confident email that: thanks them
for the idea; notes it's outside the current scope (without blaming); offers 2
options, (a) add it now for [PRICE / TIME IMPACT I'LL PROVIDE] or (b) park it for a
later phase; and asks them to confirm which option they prefer before I start. Under
170 words, in my voice.
```

Templates and advice: [scope creep emails that protect the relationship](/blog/scope-creep-email-templates/).

## Money

### 9. Invoice cover email

```text
Write a short email to accompany invoice [INVOICE NUMBER] for [AMOUNT], covering
[WHAT IT COVERS], due [DUE DATE]. Include the payment link [PAYMENT LINK], a one-line
thank-you tied to the work, and a note to reply if anything looks wrong. Under 80 words.
```

### 10. Responding to a discount request

```text
A client asked for a lower price: """[REQUEST]""". Draft a reply that acknowledges
their budget, restates the value tied to their goals, and offers these options only:
[MY OPTIONS]. If I've chosen not to reduce the price, say so kindly and clearly.
Under 150 words, confident, no apology spiral, in my voice [VOICE PROFILE].
```

For overdue invoices, use a set schedule rather than improvising: see [the five-stage payment reminder schedule](/blog/payment-reminder-schedule/).

## Finishing well

### 11. Project wrap-up and handover

```text
Write a project wrap-up email: thank the client; list final deliverables and where
to find them """[DELIVERABLES AND WHERE THEY ARE]"""; access changes """[ACCESS
CHANGES]"""; what support is included afterwards per """[SUPPORT TERMS]"""; how to
reach me for future work; and a note that the final invoice (if any) follows
separately. Under 200 words, warm and organized.
```

### 12. Testimonial request

```text
Draft a short email asking a client for a testimonial after we finished [PROJECT].
Make it easy: offer 3 optional questions (What was the situation before? What was it
like working together? What changed afterwards?); say it can be 2–3 sentences; ask
permission to publish it with their name and business (or anonymously, their choice);
and say I'll send them the final wording to approve before it appears anywhere.
Under 140 words, in my voice [VOICE PROFILE].
```

Always get permission, publish testimonials as given (edited only with the client's approval), and never write one yourself.

## Three habits that make these work

1. **Fill every placeholder, or delete that part.** A placeholder left for the AI to fill is an invitation to invent.
2. **Read every draft before sending.** Check names, dates, amounts and promises.
3. **Save your best outputs as templates.** Use AI for the personalized first lines and your template for the rest.

**Where these come from:** all twelve are from *The Band of One Prompt Library*, which has 100 prompts across 11 categories, each with an objective, inputs, output format and tips.
