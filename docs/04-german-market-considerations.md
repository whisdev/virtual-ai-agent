# German Market Considerations (DACH)

Factors to discuss during consultation when building for the German-speaking market.

## Legal & Compliance

### DSGVO (GDPR)

- **Data processing** — Where is user/lead data stored? EU vs. non-EU?
- **Consent** — Lead capture, marketing emails, cookies: explicit consent required
- **Right to deletion** — Can users request data removal? How do agents handle this?
- **Data minimization** — Only collect what's necessary for the stated purpose

### AI-Specific Regulations (EU AI Act)

- **Risk classification** — Is this "limited risk" or "minimal risk"? 
- **Transparency** — Users must know they're interacting with AI
- **Human oversight** — Critical decisions (e.g., lead qualification) may need human review

## Language & Localization

### German Language Quality

- **Formal vs. informal** — German uses "Sie" (formal) vs. "Du" (informal); B2B typically "Sie"
- **Model choice** — Some models perform better in German; consider multilingual vs. German-focused
- **SEO** — German search behavior differs; compound words, long-tail queries

### Regional Nuances

- **DACH** — Germany, Austria, Switzerland: similar but not identical (e.g., Swiss German, Austrian terms)
- **Business culture** — More formal, documentation-heavy, compliance-aware than some other markets

## Business Practices

### B2B Expectations

- **Documentation** — Contracts, terms, data processing agreements (AV-Vertrag)
- **Invoicing** — Reverse charge, VAT handling for EU cross-border
- **Support** — German-speaking support often expected

### Marketing & Lead Gen

- **Double opt-in** — Standard for email lists in Germany
- **UWG** — Unfair competition law; strict rules on cold outreach
- **Trust signals** — Impressum, Datenschutzerklärung, clear contact info

## Technical Implications

| Area | Consideration |
|------|---------------|
| **Hosting** | Prefer EU data centers (e.g., Frankfurt, Amsterdam) |
| **APIs** | Check if third-party APIs (CRM, ads) support EU data residency |
| **Logging** | Avoid logging PII; anonymize where possible |
| **Model providers** | Some offer EU endpoints; verify data processing locations |

## Questions for Consultant

1. Have you built systems for EU/German compliance before?
2. What's your experience with DSGVO in AI/agent contexts?
3. Any recommendations for German-language LLM performance?
4. Integration with German CRM/marketing tools (e.g., HubSpot DE, Mailingwork)?
