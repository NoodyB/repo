---
title: "How to Keep Client Data Private When You Use ChatGPT, Claude or Gemini"
description: "A privacy routine for using AI with client work: what never to paste, how to redact, and which ChatGPT, Claude and Gemini settings to check."
slug: client-data-privacy-ai
category: ai-done-right
date: 2026-09-24
updated: 2026-09-24
review_type: researched
tested_note: "Settings described from each provider's official help pages as checked on 24 September 2026. Menus change often; check the linked pages before relying on them."
status: ready-for-review
tags: [privacy, AI safety, ChatGPT, Claude, Gemini]
product_cta: starter
related: [ai-business-brief, make-ai-sound-like-you, ai-prompts-for-client-emails]
sources:
  - title: "OpenAI Help Center, Data controls in ChatGPT"
    url: "https://help.openai.com/en/articles/7730893-data-controls-faq"
    accessed: 2026-09-24
  - title: "OpenAI Help Center, Temporary chat in ChatGPT"
    url: "https://help.openai.com/en/articles/8914046-temporary-chat-in-chatgpt"
    accessed: 2026-09-24
  - title: "Anthropic Privacy Center, Is my data used for model training?"
    url: "https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training"
    accessed: 2026-09-24
  - title: "Anthropic Privacy Center, How long do you store my data?"
    url: "https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data"
    accessed: 2026-09-24
  - title: "Google, Manage and delete your activity in Gemini Apps"
    url: "https://support.google.com/gemini/answer/13278892"
    accessed: 2026-09-24
  - title: "Google, Gemini Apps Privacy Hub"
    url: "https://support.google.com/gemini/answer/13594961"
    accessed: 2026-09-24
---

AI assistants are genuinely useful for client admin: drafting emails, summarizing calls, tidying proposals. But every time you paste something in, you're sharing it with a third-party service. Your clients trusted *you* with their information, not your AI provider.

This guide gives you a simple routine: **decide what never gets pasted, redact what does, and set your assistant's data controls deliberately.** It's written for solo service providers, not lawyers. If you work under specific confidentiality agreements or regulations (health, legal, financial), those rules come first. Check them, and ask the client when in doubt.

## Rule 1: Some things never get pasted

Keep these out of consumer AI chats entirely:

- **Passwords, API keys, access links with tokens**, and two-factor codes
- **Financial account details**: bank numbers, card numbers
- **Government ID numbers** and similar identifiers
- **Health, legal or HR details** about identifiable people
- Anything a client has marked **confidential**, or that your agreement says stays private

If the task genuinely needs this information, do that part by hand.

## Rule 2: Redact the rest

For everything else, replace identifying details with **placeholders** before pasting:

| Instead of | Write |
|---|---|
| Sarah Chen, Harbor Dental | [CLIENT NAME], [CLIENT BUSINESS] |
| sarah@harbordental.com | [CLIENT EMAIL] |
| Invoice 2026-014 for $4,800 | Invoice [NUMBER] for [AMOUNT] |
| Their launch date is 3 March | Launch date: [DATE] |

The assistant can write an excellent email to "[CLIENT NAME]", and you swap the real details back in before sending. Most drafting tasks don't need real names at all.

**A redaction helper.** If you're not sure you caught everything, ask the assistant to check. Paste text that's *already* been roughly redacted, not the raw version:

```text
I'm about to paste text into an AI assistant. Act as a careful privacy reviewer.
Scan the text between the triple quotes and list every item that could identify a
person or company or expose sensitive data (names, emails, phone numbers, addresses,
account numbers, prices tied to named clients, health/legal/HR details, passwords or
links with tokens). Then return a redacted version that replaces each item with a
clear placeholder like [CLIENT NAME] or [INVOICE AMOUNT]. Don't change anything else.
"""[PASTE TEXT]"""
```

## Rule 3: Set your data controls on purpose

Each major assistant lets consumer users control whether their chats may be used to improve the provider's models. Here's what the providers' own help pages said when we checked (24 September 2026). Menus move, so follow the source links if these paths don't match what you see.

### ChatGPT (OpenAI)

- **Model training:** Settings → **Data controls** → **Improve the model for everyone**. Turn it off if you don't want your conversations used to train models. OpenAI's help page says this applies to Free and Plus users.
- **Temporary chat:** start a new chat and select **Temporary**. According to OpenAI, temporary chats don't appear in your history, aren't used to improve OpenAI models, and may be kept for up to 30 days for safety purposes.
- **Business plans:** OpenAI states that, by default, it does not use content from ChatGPT Business, Enterprise or Edu workspaces to train its models.

### Claude (Anthropic)

- **Model training:** for consumer plans (Free, Pro and Max), Anthropic says it uses chats to improve its models if you **choose to allow it** in your **Privacy Settings**, if a conversation is flagged for safety review, or if you've explicitly opted in to something like a testing program. Check and set your choice in Claude's privacy settings.
- **Incognito chats:** Anthropic states incognito chats are not used to improve Claude, even if you've enabled model improvement.
- **Retention note:** if you allow training, Anthropic says it may keep data in de-identified form for up to five years in its training pipelines. Deleted chats aren't used for future training.
- **Feedback:** using the thumbs up/down buttons stores the related conversation (Anthropic says for up to five years), so avoid rating chats that contain client details.

### Gemini (Google)

- **Activity setting:** Google says turning off **Keep activity** in Gemini Apps Activity stops your future chats from being reviewed to improve Google services.
- **Even when it's off:** Google states conversations are still saved with your account for up to 72 hours to provide the service and process feedback. It also says that even with Keep activity off, or in temporary chats, chats are still used to respond to you and to help protect users and the public, including with help from human reviewers.

### What this means in practice

Turning training off is a sensible default for client work. But it **doesn't mean nothing is stored**: providers keep data for varying periods for safety, abuse prevention and service reasons. That's why redaction (Rule 2) matters more than any single setting.

## Rule 4: Consider a business plan if AI is core to your work

If you use AI daily with client material, the business tiers of these services generally come with different data terms. OpenAI, for example, says business workspaces aren't used for training by default. Compare the current terms and prices yourself; they change often.

## Rule 5: Tell clients how you use AI

A short, honest line in your onboarding materials builds trust:

> *I sometimes use AI tools to help draft and organize written work. I never paste confidential information or personal details into them, and everything you receive has been reviewed and edited by me. If you'd prefer I don't use AI tools on your project, just say so.*

Adjust it to what you actually do. If a client says no, respect it.

## A five-second check before every paste

1. Is anything here on the **never-paste** list?
2. Have I replaced **names, contact details and amounts** with placeholders?
3. Am I in the right **mode** (temporary or incognito, if I use it)?
4. Would I be comfortable if this client saw exactly what I pasted?

## Where to go next

Once your privacy routine is in place, the next step is giving your assistant the *right* context: your business, not your clients' secrets. Start with [the AI business brief](/blog/ai-business-brief/), then [make AI drafts sound like you](/blog/make-ai-sound-like-you/).
