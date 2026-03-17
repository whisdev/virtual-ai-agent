# Consultation Framework: First Meetings

Use this as an agenda and checklist for initial consultation sessions with the AI agent architecture expert.

## Session 1: Concept Review (60–90 min)

### Goals

- Validate the overall concept
- Understand consultant's experience with OpenClaw/ClawBot
- Identify immediate concerns or red flags

### Agenda

| Topic | Questions to Ask | Notes |
|-------|------------------|-------|
| **Concept validation** | Does a multi-agent "virtual company" make sense for this use case? | |
| **OpenClaw experience** | What have you built or worked on with OpenClaw/ClawBot? | |
| **Architecture fit** | How would you map our agents (marketing, SEO, content, leads) to an OpenClaw-style architecture? | |
| **Risks** | What are the biggest risks or pitfalls we should plan for? | |
| **Alternatives** | Are there simpler approaches we should consider first? | |

### Deliverables

- Go/no-go on proceeding to architecture deep-dive
- List of topics to explore in Session 2

---

## Session 2: Architecture Deep-Dive (90–120 min)

### Goals

- Align on orchestrator design
- Define agent boundaries and interfaces
- Discuss memory, context, and tool design

### Agenda

| Topic | Questions to Ask | Notes |
|-------|------------------|-------|
| **Orchestrator** | Single LLM vs. dedicated process? How does OpenClaw's gateway map here? | |
| **Agent design** | One agent per domain vs. combined? How do agents communicate? | |
| **Memory** | Shared SOUL/MEMORY-style vs. per-agent? What persists across sessions? | |
| **Tools** | What tools does each agent need? How do we avoid overlap? | |
| **Stack** | TypeScript/Node? Python? Model-agnostic design? | |

### Deliverables

- High-level architecture diagram (agreed)
- List of open technical decisions
- Suggested next steps (prototype vs. spec vs. PoC)

---

## Session 3: German Market & Roadmap (60 min)

### Goals

- Cover market-specific requirements (DSGVO, localization)
- Align on development phases
- Discuss engagement model for Phase 2

### Agenda

| Topic | Questions to Ask | Notes |
|-------|------------------|-------|
| **German market** | What should we consider for DACH? Language models? Compliance? | |
| **MVP scope** | What's the smallest useful version we could build first? | |
| **Timeline** | Realistic phases? Dependencies? | |
| **Engagement** | If we proceed to development, what would collaboration look like? | |

### Deliverables

- Prioritized feature list for MVP
- Rough timeline
- Decision on Phase 2 engagement (if applicable)

---

## Preparation Checklist (Before Session 1)

- [ ] Share technical concept document in advance
- [ ] Share job description (so consultant knows the context)
- [ ] Prepare 2–3 specific questions from your own research
- [ ] Have calendar ready for follow-up sessions

## Post-Consultation

- [ ] Summarize key decisions and open questions in writing
- [ ] Share summary with consultant for validation
- [ ] Decide on next step: prototype, full spec, or pause
