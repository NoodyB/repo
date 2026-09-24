---
title: "How to Write a Proposal with AI That Doesn't Sound Generic"
description: "Use ChatGPT, Claude or Gemini to draft specific, persuasive client proposals from your discovery notes, without letting AI set your prices or promises."
slug: write-a-proposal-with-ai
category: client-workflows
date: 2026-09-24
updated: 2026-09-24
review_type: guide
status: ready-for-review
tags: [proposals, AI prompts, sales]
product_cta: prompts
related: [ai-business-brief, scope-creep-email-templates, ai-prompts-for-client-emails]
sources:
  - title: "Anthropic, Prompting best practices (Be clear and direct)"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
    accessed: 2026-09-24
  - title: "OpenAI Help Center, Prompt engineering best practices for ChatGPT"
    url: "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt"
    accessed: 2026-09-24
---

Ask an AI assistant to "write a proposal for a website redesign" and you'll get something that could be sent to anyone, which means it persuades no one. The fix isn't a better adjective in the prompt. It's **better inputs**: your discovery notes, your business context, and a proposal structure that forces specificity.

This guide shows the structure, the prompt and the review step that turn AI into a fast first-draft writer for proposals that sound like you and fit the client in front of you.

## Why AI proposals sound generic

AI assistants fill gaps with the most typical content. If the prompt doesn't say what the client told you, what you'll deliver, what's excluded, and how you write, the assistant supplies the average of every proposal it has seen.

The prompting guides from both Anthropic and OpenAI make the same point: be specific about context, the outcome you want and the format. Anthropic suggests imagining the AI as "a brilliant but new employee who lacks context on your norms and workflows". You wouldn't hand a new employee one sentence and expect a good proposal either.

## Step 1: Capture the right discovery notes

The proposal is only as specific as your notes. After (or during) a discovery call, capture:

- **Their situation in their words**: what's happening now, and why now
- **The outcome they want**: what will be different when this works
- **Constraints**: budget signals, deadline, decision-makers, anything already tried
- **Scope signals**: what they assume is included that you'll need to address
- **Quotes worth reusing**: a phrase they used about the problem

If you record calls, a transcript works too, but redact names and confidential details before pasting it anywhere (see [keeping client data private with AI](/blog/client-data-privacy-ai/)).

## Step 2: Use a seven-part structure

A structure stops the assistant from padding and makes your proposals consistent:

1. **Their situation**: two or three sentences in the client's words
2. **Outcomes**: what will be different when you're done
3. **Scope**: deliverables as a numbered list
4. **Not included**: explicit exclusions (your best defense against [scope creep](/blog/scope-creep-email-templates/))
5. **Timeline**: milestones and what you need from the client at each one
6. **Investment**: price, payment schedule and what's included. **You write this part.**
7. **Next step**: exactly how to say yes

## Step 3: The prompt

```text
Here is my business brief and voice profile: [PASTE]. And my discovery call summary
(redacted): """[SUMMARY]""". Draft a proposal using this structure: 1) Situation
(2-4 sentences using the client's words), 2) Outcomes (3-5 bullets), 3) Scope (numbered
deliverables), 4) Not included (3-6 bullets), 5) Timeline (milestones), 6) Investment:
[PRICE / OPTIONS I'LL PROVIDE]. Use exactly my prices and payment terms and don't invent
any. 7) Next step. Keep it under 700 words, plain language, no buzzwords. Mark anything
you had to assume with [CHECK].
```

Three details matter:

- **"Use exactly my prices… and don't invent any."** Pricing is a business decision. If you haven't set a price, leave the section as a placeholder and fill it yourself.
- **"Mark anything you had to assume with [CHECK]."** This turns hidden guesses into visible questions.
- **The business brief and voice profile.** Without them, the draft sounds like a template. With them, it sounds like you. Build yours once with [the AI business brief method](/blog/ai-business-brief/).

## Step 4: Offer options (you set the numbers)

Many clients find it easier to choose between options than to accept or reject a single price. A simple three-option structure:

| Option | What it is | Why it helps |
|---|---|---|
| Essential | The core outcome, minimal extras | A clear entry point |
| Recommended | What you'd advise, based on the call | The option you explain best |
| Extended | Adds support, speed or extra deliverables | Shows the full range |

Ask the assistant to **describe** each option from your notes, then add the prices yourself.

## Step 5: Review before sending

Read the draft once for each of these, and don't skip it:

- [ ] Every price, date and deliverable is one you chose
- [ ] Nothing is promised that you can't control (results, rankings, revenue)
- [ ] Every [CHECK] marker is resolved or deleted
- [ ] At least one detail could only apply to this client
- [ ] Exclusions are specific ("copywriting for new pages" rather than "extra work")
- [ ] The next step is one clear action

Then read the Situation section aloud. If it doesn't sound like something you'd say on a call, rewrite it by hand.

## A quick example

Here's a fictional web designer's discovery note, "They said their current site 'looks like 2015' and they lose leads because the contact form breaks on phones", becoming a Situation paragraph:

> *Your current site was built several years ago and no longer reflects the business you run today. More urgently, the contact form doesn't work reliably on phones, so some of the people trying to reach you are giving up before you ever hear from them.*

Specific, in the client's terms, and no invented statistics.

## Follow up without sounding pushy

Send the proposal with a short note naming the one decision you need, then follow up three to four business days later if you haven't heard back. The [12 AI prompts for client emails](/blog/ai-prompts-for-client-emails/) include a follow-up that adds something useful instead of just "checking in".

**The takeaway:** AI writes proposal first drafts fast when you give it the client's words, a structure and firm guardrails. You keep the parts that matter most: price, promises and the final read.
