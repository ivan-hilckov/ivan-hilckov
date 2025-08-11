## Goal

Make the English short resume (`README.md`) concise, targeted for the English‑speaking job market, compatible with LinkedIn/ATS, and well‑presented in Markdown, using factual content from `CV.md`.

## Gaps Identified

- Missing or suboptimal targeting
  - No explicit target roles or regions; lacks “open to remote/relocation” and time zone
  - No work authorization statement (if applicable) and no LinkedIn profile link
- Concision issues
  - Too many sections; some are verbose for a “short resume”
  - Project blurbs and domain details are lengthy vs. a 300–400 word target
- LinkedIn/ATS compatibility
  - Heavy Markdown sections and an image block (YouTube thumbnail) won’t carry into LinkedIn profile fields
  - Mixed punctuation and date styles; LinkedIn prefers simple bullets and consistent date formats (e.g., Jan 2023 — May 2024)
  - Some claims conflict with CV (e.g., Selenium test metrics), risking ATS/reviewer trust
- Presentation and content hygiene
  - Instagram and non‑professional links in Contact section; missing LinkedIn link
  - Broken Lightroom links (archive not present in repo); two different targets for xmp.zip
  - Inconsistent company coverage (README omits several companies yet duplicates lower‑signal content elsewhere)

## Target Positioning (to reflect in README)

- Primary roles: Lead Frontend Engineer, Staff Frontend Engineer (React/Next.js)
- Secondary roles: Full‑stack Engineer (React + Node.js/FastAPI)
- Region & work mode: English‑speaking market (EU/UK/US), remote‑first; add explicit UTC+3 time zone
- Add authorization/relocation only if applicable (user confirmation required)

## Proposed README Structure (LinkedIn/ATS‑friendly, <= 400 words)

1. Header
   - Name, title (Lead Frontend Engineer), location “Moscow, Russia (UTC+3)”, links: Email, GitHub, LinkedIn, Website
2. Professional Summary (3–4 sentences)
   - 17+ years; React/Next.js focus; performance at scale; team leadership; domains: video streaming, geospatial; delivery record
3. Selected Achievements (4–6 bullets, each with clear metric)
   - Anti‑scraping traffic reduction 75% (Tekara)
   - SSR/edge + caching optimization supporting up to ~70,000 RPS (Tekara)
   - Latency reduction ~40% during high traffic events (START.ru)
   - 800+ Selenium E2E tests improving release stability (Skyeer) [align with CV wording]
   - Sber500 Top‑100 (HRONIKA)
4. Experience (3 roles max, 1–2 bullets each)
   - HRONIKA — Co‑Founder — Apr 2025 — Present — brief scope + 1 metric
   - START.ru — Lead Frontend Engineer — Jan 2023 — May 2024 — 1–2 metrics
   - Skyeer — Lead Frontend Engineer — Apr 2017 — Jan 2023 — 1–2 metrics
5. Core Skills (ATS keywords on one line per category)
   - Frontend: React, Next.js, TypeScript, Redux, React Native
   - Backend: Node.js, FastAPI, Flask; DB: PostgreSQL, Redis
   - Tooling: Docker, CI/CD, Cypress, Jest
   - Domains: Geospatial (Cesium/Mapbox/Leaflet/Potree), Media (FFmpeg, HLS)
6. Education (one line)

Notes:

- Avoid images, tables, and complex Markdown. Use simple bullets and minimal bold/italics so it pastes cleanly into LinkedIn.
- Keep company names and job titles bold; dates in italics or plain consistent format.

## Concrete Edit List for README.md

1. Contact block
   - Remove Instagram; add LinkedIn profile link (once provided)
   - Keep Email, Telegram (optional), GitHub; consider adding website/portfolio
2. Executive Summary → compress into a 3–4 sentence Professional Summary focused on target roles and value
3. Replace or prune lengthy sections
   - Replace “Technical Competencies” with compact “Core Skills” per categories above
   - Move “Research Interests” off the short resume (optional: keep in repo, not in README)
   - Keep “Personal Projects” only if they showcase target stack; limit to 2–3 items with stack tags
   - Replace “Portfolio Demonstration” image with a single hyperlink to the video demo
4. Experience normalization
   - Keep only HRONIKA, START.ru, Skyeer (most relevant/high‑signal); compress to 1–2 bullets each with metrics
   - Standardize dates to `Mon YYYY — Mon YYYY`; ensure ASCII hyphen/en dash consistency
   - Ensure claims align with `CV.md` (e.g., Selenium coverage/stability numbers)
5. Achievements section (new)
   - Add a concise metric‑first bullet list (4–6 bullets), sourced from `CV.md`
6. ATS/LinkedIn alignment
   - Use simple `-` bullets; avoid tables and images
   - Prefer standard tech names/keywords for parsing (React, Next.js, TypeScript, Node.js, FastAPI, PostgreSQL, Redis, Docker, CI/CD, Cypress, Jest)
7. Links hygiene
   - Remove or fix Lightroom `xmp.zip` links (no `xmp.zip` artifact in repo)
   - Option A: remove from README; keep in dedicated “Lightroom Presets” section after adding a real archive
   - Option B: add a small script to zip `xmp/` into `xmp.zip`, commit artifact (or attach to a GitHub Release), and update both links to the working location

## Draft Copy (for the new README layout)

### Header

Hilkov Ivan Andreevich — Lead Frontend Engineer — Moscow, Russia (UTC+3)
Email · GitHub · LinkedIn · Website

### Professional Summary

Lead Frontend Engineer with 17+ years of experience delivering React/Next.js applications at scale. Specialized in performance optimization, streaming/video, and geospatial UI. Led teams of up to 8 engineers and shipped complex products end‑to‑end, balancing technical excellence with business outcomes.

### Selected Achievements

- Reduced unauthorized scraping traffic by 75% via anti‑scraping measures (Tekara)
- Scaled SSR storefront with CDN and server caching to handle ~70,000 RPS (Tekara)
- Cut API latency by ~40% during peak traffic events (START.ru)
- Built 800+ Selenium tests with QA, significantly improving release stability (Skyeer)
- HRONIKA prototype selected into Sber500 Top‑100

### Experience (Selected)

- HRONIKA — Co‑Founder — Apr 2025 — Present
  - Built autonomous timelapse platform (Raspberry Pi, Canon 1100D, React + FastAPI)
- START.ru — Lead Frontend Engineer — Jan 2023 — May 2024
  - Launched “Cinema on TV”; optimized request patterns and reliability under peak load
- Skyeer — Lead Frontend Engineer — Apr 2017 — Jan 2023
  - Developed geospatial platform; led frontend team; integrated Cesium/Mapbox/Potree

### Core Skills

Frontend: React, Next.js, TypeScript, Redux, React Native
Backend: Node.js, FastAPI, Flask; DB: PostgreSQL, Redis
Tooling: Docker, CI/CD, Cypress, Jest
Domains: Geospatial (Cesium/Mapbox/Leaflet/Potree), Media (FFmpeg, HLS)

### Education

Kuban State University — Faculty of Theoretical Physics

## Link Fixes and Supporting Tasks

- Provide LinkedIn profile URL; add to Contact
- Decide on Instagram visibility (default: remove from short resume)
- Fix Lightroom archive links:
  - Add `scripts/zip_xmp.sh` or Python/Make task to build `xmp.zip` from `xmp/`
  - Commit artifact or attach to GitHub Release; update links to the single canonical URL
- Verify `CV.pdf` link works and keep it in README (“Full CV (PDF)”) but not in Contact block

## Implementation Steps

1. Update Contact block (remove Instagram; add LinkedIn; keep Email/GitHub/Telegram)
2. Replace Executive Summary with new Professional Summary (<= 4 sentences)
3. Add “Selected Achievements” with 4–6 metric‑first bullets (from `CV.md`)
4. Compress Experience to 3 roles with 1–2 bullets each; standardize dates and locations
5. Replace Technical Competencies with compact “Core Skills” blocks (ATS‑friendly)
6. Replace embedded image with a plain text link to the demo video
7. Remove or fix Lightroom links as per decision; if keeping, ensure archive exists
8. Proofread for US/UK English, punctuation, and consistent formatting

## Open Questions (confirm with user before finalizing)

- Work authorization (EU/UK/US) and relocation readiness
- Preferred target regions (US/EU/UK) and remote/on‑site preferences
- LinkedIn profile URL and personal website (if any)

## Acceptance Criteria

- README word count ~300–400 with 4–6 bullets of quantified achievements
- No broken links; Contact contains Email, GitHub, LinkedIn (and optional Website)
- Dates standardized, sections minimal, and content paste‑friendly into LinkedIn
- Claims aligned with `CV.md`; no contradictory metrics
