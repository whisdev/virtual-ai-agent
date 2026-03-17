# Virtuelle Agentur — Multi-Agent AI for DACH

A multi-agent AI system for the German-speaking market (DACH), designed as a virtual agency where specialized agents handle marketing, SEO, content creation, and lead management, coordinated by a central orchestrator.

## Demo

<video src="https://github.com/user-attachments/assets/353bfccb-fb25-4096-959b-0e6cb31136b9" controls width="640"></video>

---

## Purpose

**Virtuelle Agentur** (Virtual Agency) acts like a small virtual company: instead of hiring separate teams for marketing, SEO, content, and lead management, a business owner interacts with a single interface. Behind it, AI agents work together—each with a distinct role—to deliver agency-style services.

### Why This Exists

- **DACH market focus** — German-speaking businesses (Germany, Austria, Switzerland) have specific needs: formal language (Sie), DSGVO compliance, and regional nuances.
- **Unified workflow** — One request can span multiple domains (e.g., "create a blog post and optimize it for SEO"); the orchestrator coordinates across agents.
- **Scalable agency services** — Small businesses get agency-level support without the cost of a full team.

### What It Does

| Capability | Description |
|------------|-------------|
| **Marketing** | Campaign ideas, ad copy, A/B test suggestions, channel strategy |
| **SEO** | Keyword research, meta tags, sitemap structure, on-page optimization |
| **Content** | Blog posts, social captions, product descriptions, landing pages |
| **Lead Management** | Lead qualification, follow-up sequences, CRM updates, scoring |

---

## Architecture

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    User / Business Owner                          │
│              (single point of contact)                           │
└────────────────────────────┬────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Central Orchestrator Agent                        │
│  • Receives user requests                                         │
│  • Routes to specialist agent(s)                                  │
│  • Aggregates and returns results                                 │
│  • Manages workflow state and context                             │
└────────────────────────────┬────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Marketing   │      │     SEO      │      │   Content     │
│    Agent     │      │    Agent     │      │    Agent      │
└──────────────┘      └──────────────┘      └──────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                    ┌──────────────┐
                    │ Lead Mgmt    │
                    │   Agent      │
                    └──────────────┘
```

### Orchestrator

The orchestrator is the **single interface** for the user. It:

- **Routes** — Analyzes each request and decides which agent(s) should handle it (e.g., "create blog + optimize SEO" → Content + SEO).
- **Coordinates** — For multi-step workflows, passes context between agents and sequences their work.
- **Aggregates** — Combines specialist outputs into a coherent response.
- **Manages state** — Tracks sessions, ongoing work, and dependencies.

### Specialist Agents

Each agent has a **narrow domain** and **specific tools**:

| Agent | Responsibility | Example Outputs |
|-------|----------------|-----------------|
| **Marketing** | Campaigns, messaging, targeting | Ad copy, A/B variants, channel strategy |
| **SEO** | Search visibility, structure | Keywords, meta tags, sitemap suggestions |
| **Content** | Written content across formats | Blog posts, captions, product copy |
| **Lead Management** | Inbound leads, qualification | Lead scores, email sequences, CRM updates |

Agents receive **context** from the orchestrator (user preferences, prior responses, business data) and return structured results.

### Design Principles

- **Model-agnostic** — LLM calls abstracted; supports OpenAI, Anthropic, Ollama, etc.
- **Auditable** — Logging and traceability for compliance (DSGVO) and debugging.
- **Extensible** — New agents can be added without changing the orchestrator core.
- **OpenClaw-inspired** — Patterns from production agent architectures (gateway, agentic loop, memory).

---

## Project Status

**Phase:** Pre-development consultation  
**Goal:** Review concept, architecture, and technical approach with an expert before building.

---

## Quick Start (Python)

```bash
cd virtuelle-ai-agentur
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: set OPENAI_API_KEY or LLM_PROVIDER=ollama for local models
PYTHONPATH=src python3 run.py
```

**Modes:**
- `python3 run.py` — Demo request (blog + SEO)
- `python3 run.py --interactive` — Type your own requests

**LLM setup:** Uses [LiteLLM](https://docs.litellm.ai/) as model gateway. Set `LITELLM_MODEL` (e.g. `openai/gpt-4o`, `anthropic/claude-3-5-sonnet`, `ollama/llama3.2`) and the corresponding API key. Without config, agents return fallback messages.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [Job Description](docs/01-job-description.md) | Polished job posting for consultant/developer |
| [Technical Concept](docs/02-technical-concept.md) | Architecture overview for discussion |
| [Consultation Framework](docs/03-consultation-framework.md) | Agenda and topics for first meetings |
| [German Market Considerations](docs/04-german-market-considerations.md) | GDPR, DSGVO, localization |
| [OpenClaw Architecture Relevance](docs/05-openclaw-architecture-relevance.md) | How OpenClaw/ClawBot maps to this project |
| [Development Roadmap](docs/06-development-roadmap.md) | Phase timeline if development proceeds |
| [Candidate Screening Checklist](docs/07-candidate-screening-checklist.md) | Evaluation criteria for applicants |

---

## Getting Started

1. Use the job description to recruit a consultant with OpenClaw/ClawBot experience.
2. Use the consultation framework to structure initial discussions.
3. Use the technical concept as a starting point for architecture review.
4. If collaboration works, follow the development roadmap.
