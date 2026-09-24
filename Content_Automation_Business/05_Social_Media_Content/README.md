# 05 · Social media content (Month 1: content and audience)

**Status: all drafted, nothing posted or scheduled.** No social accounts have been created. Suggested handle: `@bandofonehq` (availability **not** checked on each platform).

| File | What it is |
|---|---|
| `Month1_Video_Concepts_Scripts_Captions.md` | 30 short-form video concepts, hooks, scripts (with [VISUAL] cues for talking-head or faceless), on-screen text, captions and hashtags |
| `Month1_Educational_and_Promotional_Posts.md` | 15 educational posts (8 LinkedIn text, 7 Instagram carousels) + 10 promotional posts (free resources, articles, newsletter) |
| `Hashtag_Sets.md` | Six topic hashtag sets (relevance-based; no volume data claimed) |
| `Month1_Calendar_scheduler_import.csv` | Day-by-day schedule for import into a scheduler or spreadsheet |
| `BandOfOne_60-Day_Social_Calendar.xlsx` | Both months in one tracker. Type a start date and every date updates; status dropdown; summary counts |
| `Reusable_Templates.md` | Script, caption, carousel, post and repurposing templates for future months |
| `graphics/` | 7 carousels (49 slides, 1080×1350), 10 promo cards (1080×1350), 30 video covers (1080×1920) |
| `source/` | YAML sources. Edit these, then run `python3 Build_Tools/build_social.py` |

**Month 2 (product launch)** lives in `Digital_Products_Business/08_Marketing_Campaign/`: another 30 videos, 15 educational and 10 promotional posts, and 5 launch emails. It runs after this month, so the shared accounts never post two campaigns at once.

## How a week runs (about 3–4 hours)

1. **Batch record** the week's 7 videos in one session (script on screen; 1–2 takes each).
2. **Edit** captions and on-screen text; use the matching cover from `graphics/video_covers/`.
3. **Schedule** in each platform's native scheduler, or a free scheduler tier.
4. **Post the LinkedIn/Instagram posts** on their days. Carousels are ready in `graphics/carousels/`.
5. **Reply to comments** within a day. Note questions for future content.
6. **Update the calendar status** and log numbers in the content dashboard.

## Rules

- Every link goes to one article or the starter kit, with UTM tags (`utm_campaign=content-m1`).
- No income claims, no fake testimonials, and no "I tested 50 tools". Tool facts carry their "checked" date.
- Don't post in communities where self-promotion breaks the rules.
- Replace `[link]` placeholders with live URLs only after the site is deployed.
