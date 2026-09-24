---
title: "The AI Business Brief: One Page of Context That Improves Every Prompt"
description: "Create a one-page business brief for ChatGPT, Claude or Gemini so every AI draft fits your services and policies. Interview prompt and template inside."
slug: ai-business-brief
category: ai-done-right
date: 2026-09-24
updated: 2026-09-24
review_type: guide
status: ready-for-review
tags: [AI prompts, context, custom instructions]
product_cta: starter
related: [make-ai-sound-like-you, client-data-privacy-ai, ai-prompts-for-client-emails]
sources:
  - title: "Anthropic, Prompting best practices"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
    accessed: 2026-09-24
  - title: "OpenAI Help Center, Prompt engineering best practices for ChatGPT"
    url: "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt"
    accessed: 2026-09-24
---

Most disappointing AI drafts share a cause: the assistant knows nothing about your business. It doesn't know what you sell, who you sell to, your payment terms, or that you never promise "unlimited revisions". So it guesses, and guesses sound generic.

The fix takes about 20 minutes, once: a **business brief**. It's a one-page description of your business that you give the assistant as context, so every draft starts from your reality. This guide shows you how to create it with an interview prompt, what to put in it, and how to use it without pasting it every time.

## Why context beats clever prompts

Both Anthropic's and OpenAI's prompting guides stress being specific about context and the result you want. Anthropic's version is memorable: treat the AI like "a brilliant but new employee who lacks context on your norms and workflows". A new employee with a one-page briefing writes better emails than a new employee with none, and so does an AI assistant.

## What goes in a business brief

Six short sections, under about 450 words in total:

1. **Who I am**: what you do, for whom, and where
2. **Services**: your 2–4 core services and typical project size
3. **Ideal clients**: who's a great fit, and who isn't
4. **How I work**: communication hours, response times, meeting preferences, tools
5. **Policies**: payment terms, deposits, revisions, cancellations
6. **Tone and words to avoid**: phrases you never use, promises you never make

It contains **your** business information, not client information. That's important for privacy (see [keeping client data private with AI](/blog/client-data-privacy-ai/)).

## Build it with an interview prompt

Rather than writing it from scratch, let the assistant interview you. Paste this into ChatGPT, Claude, Gemini or Copilot:

```text
Help me write a one-page "business brief" I can give an AI assistant before asking
for help with client admin. Interview me with one question at a time (wait for each
answer) covering: what I do and for whom; my 2–4 core services and typical project
size; how I like to work (communication hours, response times, meeting preferences);
my payment terms and policies; phrases or promises I never want used; and three
examples of great client outcomes (described generally, no client names). When we're
done, output the brief in this format: ## Who I am, ## Services, ## Ideal clients,
## How I work, ## Policies, ## Tone and words to avoid. Keep it under 450 words.
```

Answer in your own words. Short answers are fine, and the assistant will ask follow-ups. When it outputs the brief, **edit it**: correct anything it inferred wrongly and delete anything you wouldn't say.

## An example (fictional)

> **## Who I am**
> I'm Sam, a freelance web designer in Leeds working with local service businesses (clinics, trades, studios) that need a clear, fast website.
>
> **## Services**
> - Small business websites (5–10 pages), typically 4–6 weeks
> - Website care plans (monthly updates and backups)
> - One-off fixes and improvements
>
> **## Ideal clients**
> Owner-run businesses that want more enquiries, not awards. Not a fit: e-commerce stores with hundreds of products; agencies wanting white-label work.
>
> **## How I work**
> Email for decisions; I reply within one business day, Mon–Thu. Weekly update every Friday. Calls by appointment via my booking link.
>
> **## Policies**
> 40% deposit before work starts; 14-day payment terms; two revision rounds per stage; extra work quoted before it starts.
>
> **## Tone and words to avoid**
> Friendly, plain, direct. Never: "synergy", "world-class", guaranteed rankings or results, exclamation marks in client emails.

## How to use it

**Option 1: paste it when needed.** Many prompts start with "Here is my business brief: [PASTE]". Keep the brief in a note you can copy from quickly.

**Option 2: save it as standing instructions.** Most assistants let you save instructions that apply to every chat (often called custom instructions, personalization or project instructions). A prompt to compress your brief into that format:

```text
Using my business brief and voice profile below, write standing instructions for my
AI assistant in under [CHARACTER LIMIT] characters. Split them into two parts:
(1) "What you should know about me" (business facts, services, policies) and
(2) "How you should respond" (tone, format preferences, rules). Always include these
rules: never invent prices, dates or facts about clients; mark missing information as
[NEED INFO]; keep client emails under 200 words unless I ask otherwise; suggest one
clarifying question when my request is ambiguous. Count the characters and confirm
the total.
```

Those four rules are worth keeping even if you change everything else. They stop the most common AI mistakes in client work: invented details, missing information hidden behind confident prose, and emails that are far too long.

## Add a voice profile next

The brief tells the assistant *what* your business is. A **voice profile** tells it *how you write*: your sentence length, greetings, sign-offs and the things you never do. Together they make drafts that need light edits rather than rewrites. [Here's how to build a voice profile from your own emails](/blog/make-ai-sound-like-you/).

## Keep it current

Review the brief every few months, or whenever your services, prices or policies change. An outdated brief is worse than none, because the assistant will confidently repeat old terms.

## Put it to work

With a brief in place, try it on the tasks that eat the most time: replying to inquiries, drafting proposals, weekly updates. The [12 AI prompts for client emails](/blog/ai-prompts-for-client-emails/) are all designed to use it.
