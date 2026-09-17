# Ivan Hilkov

**Lead AI Engineer — Agent Orchestration, Prompt & Context Engineering**

_AI-native engineering lead: spec-first, agent-driven, review-gated delivery with Claude Code across 4 organizations · 17 years in software_

## Contact

[strange.mole@gmail.com](mailto:strange.mole@gmail.com) • [linkedin.com/in/ivan-hilkov-a1022154](https://www.linkedin.com/in/ivan-hilkov-a1022154/) • [t.me/mrbzzz](https://t.me/mrbzzz) • [github.com/ivan-hilckov](https://github.com/ivan-hilckov) • [CV.pdf](https://github.com/ivan-hilckov/ivan-hilckov/raw/main/CV.pdf) · [CV_FULL.pdf](https://github.com/ivan-hilckov/ivan-hilckov/raw/main/CV_FULL.pdf)  
Bangkok, Thailand (UTC+7) · remote-first · open to international contracts

## Professional Summary

AI engineer who has run software delivery for 4 organizations through Claude Code since autumn 2025: YokeLoop (founder), 3 client engagements and a 5-server pool with self-hosted LLM infrastructure. Recurring prompts became versioned Agent Skills; the skills became a ticket-driven agent orchestrator that moves each change from a product requirements document (PRD) to a plan, agent implementation, a review pass and a ship step. I keep the specification, the acceptance criteria, the deep code reviews and the single confirmation before merge. Guardrails are enforced, not requested: PreToolUse hooks block irreversible operations, every refusal of the orchestrator's guard is logged, and per-ticket metrics feed back into the prompts. 17 years in frontend and full-stack engineering (TypeScript, React, Go, Python), 9 of them leading teams of up to 8, are what make the reviews deep and the specifications precise.

## AI Engineering Projects

**yokemate — ticket-driven multi-agent orchestrator on Claude Code** (YokeLoop, _Aug 2026 — Present_)

- Orchestrates tickets from 3 YouTrack instances and GitHub Issues across 4 organizations from one Claude Code session. Each ticket passes a 6-stage lifecycle (new, scouted, planned, running, review, accepted) held in a shared PostgreSQL queue, so the laptop and 3 pool servers act as equal peers.
- Gates implementation: tests before code where a suite exists, the project's own checks, a review pass by a separate subagent, a simplification pass, a documentation sync and one PR per affected repository; a human confirms once per ticket, before merge. Built from 12 engineer-facing skills (/plan, /do, /review, /ship), 6 worker skills and 9 subagents (scout, planner, executor, reviewer, retrospective).
- Governs least-privilege tool access per mode (research panes cannot write code or move queue state), routes read-only subagents to a cheaper model tier, and carries context through 9 Model Context Protocol (MCP) servers (YouTrack, Figma, Dokploy, SSH, PostgreSQL) and CLAUDE.md in 28 of 39 working clones.
- Instrumented from its own journal and transcripts (Aug 15 to Sep 17, 2026): 125 tickets from plan to merge at a median of 14 hours, 45% of tickets with no human intervention, a PR link on 188 of 188 execution reports, agent cost per ticket at a median of $10 (75th percentile $18) over 87 tickets with recorded cost, about $3,200 of tracked spend for the month, half of it in sessions outside any ticket; a retrospective skill turns journals, transcripts and guard traces into accepted or declined prompt changes. 977 commits, 289 automated tests, v2.0.0 after one month.
- Fourth generation of one pipeline in 7 months: a homegrown skills pack, the public plugin [yoke](https://github.com/yokeloop/yoke) (14 commands and the `.yoke/` artifact convention: glossary, decision records, per-task PRD, plan and report), a captain-and-crew harness forked from the open-source Firstmate and piloted on disposable git worktrees, then the orchestrator above, now being ported to a second agent runtime (Pi). Each rewrite answered a failure of the previous one, starting from 300-line plans and 100-file diffs that nobody could review.

**Guardrails for autonomous agent sessions** (_Aug 2026 — Present_)

- Wrote a Bash PreToolUse hook with a regex denylist of irreversible operations (firewall reset, docker prune with volumes, filesystem formatting) that also catches the same commands wrapped in `ssh host '…'`, so one guard on the workstation covers all 5 pool servers; block and pass fixture tests.
- In the orchestrator every refusal names the allowed alternative and appends one JSON line to an audit log (228 entries in the first 10 days of logging: 202 denials, 26 confirmations) that feeds the metrics and the retrospective. Damage is bounded to the ticket's disposable worktree, so the guard fails open on its own errors instead of halting the pipeline.

**Self-hosted AI platform on a 5-server pool** (YokeLoop, _May 2026 — Present_)

- Runs 5 machines (Ubuntu, Arch, Debian; Singapore, US, Netherlands) on a Tailscale mesh with a machine-readable inventory, per-machine profiles for agents, reboot and upgrade policies and 4 pool-administration skills; admin surfaces reachable from the tailnet only.
- Runs 10 services from 14 versioned Dokploy blueprints: a LiteLLM gateway exposing one OpenAI-compatible API over cloud and local models with per-client virtual keys, Open WebUI with SearXNG search, a GPU box for Whisper, embeddings and ComfyUI, self-hosted Supabase with pgvector, MinIO, Mattermost, n8n and Vaultwarden; Uptime Kuma (23 checks) and a weekly fleet report to Mattermost watch it.

## Key Metrics (June 2025 — September 2026)

- Throughput with a quality denominator: 5,700+ attributed commits and 888 pull requests (828 merged, 93%) across 96 repositories in 8 organizations in 15 months, with 4 reverts among the 4,076 commits analyzed locally.
- Context engineering: 38% of commits change only Markdown or agent-configuration files (plans, journals, skills, CLAUDE.md); about 30 skills, 14 plugin commands and 9 subagent definitions authored, versioned and released through git.

![GitHub Contribution Graph](https://ghchart.rshah.org/ivan-hilckov)

_About 1,500 commits from June to August 2026 carry a mistyped git email and are not attributed to the account, so the graph undercounts._

## Professional Experience

### **YokeLoop** — **Founder, AI Engineering Lead** — _Apr 2026 — Present_ (tooling line since Feb 2026)

- Built the agent tooling and the self-hosted platform described above and, from February 2026, delivered the client work below through them; 1,630 commits in 29 repositories, 189 PRs.
- Built the provisioning layer of hermes-orchestration, a partner-designed B2B platform for hosting isolated AI agents on bare metal: provisioning service with presets, LiteLLM virtual-key issuance, provisioner UI, credential-rotation runbook, gateway smoke tests.
- Shipped nook, a Telegram Mini App social product, as sole developer: 3 deployable apps in a pnpm monorepo, 52 test files run in CI against a real PostgreSQL database, prebuilt images on GitHub Container Registry deployed with Dokploy; 213 commits, 52 PRs.

### **Talking Birds & Flying Fish (TB-FF)** — **Lead Engineer, Electron kiosk platform** — _Oct 2025 — Present_

_Production studio building interactive installations for corporate conference stands and museum exhibits (client engagement; end customers under NDA)_

- Owned the studio's Electron kiosk template (auto-update, release gate, Telegram release notifications) and co-authored the shared React library `@tb-ff/web-toolkit`, from which the studio's later event and museum apps are stamped (14 app repositories).
- Delivered the player-station software for a security vendor's game arena at a major US industry conference (March 2026): 5 stations, a 27-screen flow, 3 timed touch games, an offline SQLite buffer synced to a Supabase leaderboard, plus the live leaderboard display and a moderation panel.
- Architected a two-PC, server-authoritative room simulator for a conference installation as a server app, a client app and a shared typed LAN protocol package (Arduino buttons and lights); both apps released at v2.0.6.
- Contributed the test and reliability layer to a museum's 8-installation children's exhibit (Playwright runtime, visitor walkthroughs, load and endurance tests, error screen with retry) and built the delivery-robot kiosk over WebSocket and a COM port; CLAUDE.md in every repository, agent skills in the template, `.yoke/` plans and review reports in the simulator and museum repositories; 1,990 commits in 22 repositories, 313 PRs opened, 37 reviewed.

### **Velvet VPN (velvetnet)** — **Lead Frontend Engineer, AI-driven delivery** — _Apr 2026 — Present_

_VPN subscription business: Telegram bot, subscriber portal, public subscription page, UI kit, CRM (client engagement)_

- Created the public subscription page from an empty repository: runs in the browser and as a Telegram Mini App, API-driven setup guides, white-label mode for resellers, CI on every PR, Playwright end-to-end tests against offline and live environments; 110 PRs merged, deployed through GitHub Actions to Kubernetes.
- Created `@velvetnet/vpn-ui-kit` (44 minor releases) consumed by 3 apps; co-developed the subscriber portal (saved cards behind a feature flag, API-driven FAQ, Sentry hardening).
- Prototyped a Chrome Manifest V3 VPN extension with its own Fastify and SQLite backend (email login, device identity, PAC routing, event telemetry, release pipeline) in 5 weeks.
- Prototyped an evaluation loop for the support CRM's LLM replies: retrieval-augmented generation (RAG) over the knowledge base with pgvector and a promptfoo endpoint scoring reply quality with an LLM-as-judge; 228 PRs opened in the organization.

### **PokerNode** — **Frontend Lead** — _Dec 2025 — Aug 2026_

- Led the frontend of a real-time React 19 poker client (WebSocket and EventSource) for a partner studio: history lobby and replay viewer, table-engine visuals in 6 staged PRs, mobile tables readable at 360 to 414 px, SEO for the prerendered landing; 377 commits, 57 PRs merged.

### **ALMATICA** — **Lead Developer & Tech Lead** — _Aug 2025 — Sep 2025_

- Audited 3 legacy projects and unified them into a microservices MVP (Go API, React 18 frontend, Python LangGraph and LangChain services, Docker Compose) in 1 month; led 3 developers and set up planning, reviews and CI/CD.

### **Bot Garden** — **Founder** — _Jun 2025 — Sep 2025_ · **HRONIKA** — **Co-Founder** — _Apr 2025 — Sep 2025_

- Built 4 LLM-backed Telegram bot prototypes in 2 months on the OpenAI, Perplexity and Anthropic APIs with a shared runtime deployed through GitHub Actions; co-founded a Raspberry Pi timelapse system for construction monitoring (React dashboard, FastAPI and Celery backend).

### **Tvigle** — **Lead Frontend Engineer** — _May 2024 — Oct 2024_

- Online cinema: ad SDK integrations (Yandex Ads, VK Ads) via MRAID, VAST 2.0 to 4.0 upgrade, React Native mobile app.

### **START** — **Lead Frontend Engineer** — _Jan 2023 — May 2024_

- Cut API P95 latency by 40% through query and caching optimization on a streaming platform peaking at 700,000 requests per second; built the Next.js "Movies on TV" and "TV Series" sections; led 4 engineers.

### **Skyeer** — **Lead Frontend Engineer** — _Apr 2017 — Jan 2023_

- Web-GIS platform for drone data: an MVP in 3 months won 1st place at the Gazprom "Unmanned Biathlon" (accuracy of ±0.02 m³) and 10+ enterprise contracts; resumable uploads up to 100 GB (tus.io); 800+ Selenium E2E tests improved release stability by 80%; led 8 engineers.

**Earlier roles**: Amediateka — Senior Frontend Engineer, SVOD platform on Next.js (_2019_); Ivideon, REKOD, Liga Stavok, OneTwoTrip — senior and mid-level frontend, jQuery and Backbone to React and Redux (_2015 — 2017_); Sovzond — "Satellite Imagery Archive" SPA, first QA process (_2013 — 2015_); 5 earlier frontend and system-administration roles (_2008 — 2013_).

## Technical Skills

- **Agent platform & prompt engineering**: Claude Code (Agent Skills with SKILL.md, hooks: PreToolUse, SessionStart, UserPromptSubmit; subagents; plugins; CLAUDE.md, AGENTS.md), MCP servers, context engineering, prompt engineering, spec-driven development, agent orchestration (orchestrator-workers, reviewer and rework loops, human-in-the-loop gates), model routing by role, Codex CLI, Pi (pi.dev agent runtime)
- **Evals, guardrails & observability**: PreToolUse guards with audit logs, least-privilege tool permissions per mode, promptfoo with LLM-as-judge, RAG with pgvector, per-ticket cost and stage metrics, LLM-driven retrospectives, Uptime Kuma, Sentry
- **LLM infrastructure**: LiteLLM, Open WebUI, SearXNG, GPU inference (Whisper, embeddings, ComfyUI), pgvector, Supabase, MinIO, Dokploy, Docker Compose, Traefik, Tailscale, n8n
- **Delivery tooling**: YouTrack (REST and MCP), GitHub CLI, GitHub Actions, Playwright, Cypress, git worktrees
- **Product stack**: TypeScript, React 19, Electron, Vite, Next.js, Telegram Mini Apps, Chrome Manifest V3, Fastify, Node.js, Bun, Python, Go, PostgreSQL, SQLite, Redis, WebSocket, gRPC, Kubernetes
- **Languages**: Russian (native), English (professional working proficiency)

## Speaking & Open Source

- Seminar "AI and LLM for researchers": one day, 53 slides, FBU VNIILM (federal forestry research institute), 13 May 2026 — [slides](https://github.com/ivan-hilckov/seminar-ai-llm)
- [yokeloop/yoke](https://github.com/yokeloop/yoke) — Claude Code plugin and marketplace of skills and commands for the full development loop; [projectory-com/sp](https://github.com/projectory-com/sp) — its predecessor
- [heliotik/botglue.nvim](https://github.com/heliotik/botglue.nvim) — Neovim plugin for AI-assisted inline code editing via the Claude Code CLI

## Education

**Bachelor of Science in Theoretical Physics** — Kuban State University, 2010

## Availability & Preferences

- Immediately available for Lead AI Engineer, Applied AI Engineer, Forward Deployed Engineer and AI-native engineering lead roles; remote-first, open to hybrid arrangements, relocation and international contracts
