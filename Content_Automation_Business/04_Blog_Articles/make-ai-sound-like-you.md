---
title: "How to Make AI Drafts Sound Like You (the Voice Profile Method)"
description: "Stop AI emails sounding generic. Build a reusable voice profile from your own writing, then use it to get drafts that need light edits, not rewrites."
slug: make-ai-sound-like-you
category: ai-done-right
date: 2026-09-24
updated: 2026-09-24
review_type: guide
status: ready-for-review
tags: [AI writing, voice, client emails]
product_cta: prompts
related: [ai-business-brief, ai-prompts-for-client-emails, client-data-privacy-ai]
sources:
  - title: "Anthropic, Prompting best practices"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
    accessed: 2026-09-24
  - title: "OpenAI Help Center, Prompt engineering best practices for ChatGPT"
    url: "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt"
    accessed: 2026-09-24
---

You can usually spot an AI-written email in the first line. "I hope this email finds you well." "I'm thrilled to…" "Please don't hesitate to reach out." Clients notice too, and an email that doesn't sound like you undermines the relationship you've built.

The solution isn't to stop using AI. It's to **show the assistant how you actually write**, once, and reuse that description every time. We call it a voice profile. Here's how to build one in about 15 minutes.

## What a voice profile captures

A voice profile is a short (under 250 words) description of your writing habits:

- **Sentence length**: short and punchy, or longer and explanatory?
- **Greetings and sign-offs**: "Hi Sam," or "Hello Sam,"? "Thanks," or "Best,"?
- **Formality**: on a 1–5 scale
- **Words and phrases you actually use**
- **Things you never do**: exclamation marks, emojis, corporate phrases, over-apologizing
- **How you deliver bad news**: direct first, or context first?
- **Do / not-that examples**: short pairs that make the rules concrete

## Step 1: Pick 3–5 real emails

Choose emails you wrote yourself that represent you well, ideally a mix:

- a friendly routine update
- a reply to a new inquiry
- one with difficult news (a delay, a "no", a price conversation)

**Remove client names and details first**, replacing them with placeholders like [CLIENT NAME]. See [keeping client data private with AI](/blog/client-data-privacy-ai/) for a quick redaction routine.

## Step 2: Run the voice profile prompt

```text
Below are [NUMBER] emails I wrote to clients (names removed). Analyze my writing
style and produce a "voice profile" I can reuse in future prompts. Include: typical
sentence length; greeting and sign-off habits; level of formality (1–5); words and
phrases I use often; things I never do (e.g., exclamation marks, emojis, corporate
phrases); how I deliver bad news; and 3 short "do this / not that" examples. Keep it
under 250 words and don't invent traits that aren't in the samples.
"""[PASTE 3–5 REDACTED EMAILS]"""
```

The last instruction ("don't invent traits that aren't in the samples") keeps the profile honest. Without it, assistants tend to add flattering generalities like "warm and professional" that don't help.

## Step 3: Edit the profile

Read what comes back and fix it. Typical edits:

- Delete vague traits ("engaging", "professional") and keep specific ones ("opens with the recipient's name and one line of context").
- Add rules the samples didn't show: "Never write 'I hope this finds you well'."
- Check the do/don't examples. They're the most useful part, so make sure they're right.

### Example (fictional)

> **Voice profile: Sam**
> - Short sentences; one idea per paragraph; emails rarely over 150 words.
> - Opens "Hi [Name]," and closes "Thanks, Sam". No "Best regards".
> - Formality 2/5: friendly, never casual slang.
> - Uses: "quick update", "here's where we are", "does that work for you?"
> - Never: exclamation marks, emojis, "I hope this finds you well", "just checking in", "don't hesitate to reach out".
> - Bad news: states it in the first line, one sentence of reason, then the plan.
> - Do: "The launch will move to Thursday. Here's why and what happens next." / Not: "Unfortunately, due to some unforeseen circumstances, we may need to consider adjusting…"

## Step 4: Use it everywhere

Add the profile to any drafting prompt: "Write this in my voice: [VOICE PROFILE]". Better still, save it with your [business brief](/blog/ai-business-brief/) in your assistant's standing instructions, so it applies automatically.

## Step 5: Improve it with real edits

Each time you substantially rewrite an AI draft, ask yourself *why*. If it's a pattern ("it keeps adding a summary paragraph at the end"), add a line to the profile ("Never end with a summary of the email"). After a few weeks, drafts need much less editing.

## Common questions

**Does this work in free AI plans?** Yes. It's just text you include in a prompt.

**Should I use my most polished writing?** Use your *typical* client writing. The goal is to sound like you on a normal Tuesday, not your best marketing copy.

**Will the drafts be perfect?** No, and they shouldn't go out unread. The aim is a draft you can check and send in two minutes, not one you have to rewrite in ten.

## Put it together

A voice profile plus a business brief is the foundation for every client-facing prompt. Try both with the [12 AI prompts for client emails](/blog/ai-prompts-for-client-emails/), or on your next [weekly client update](/blog/weekly-client-update-template/).
