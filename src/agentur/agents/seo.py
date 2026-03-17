"""SEO agent — search visibility, keywords, structure."""

from ..base_agent import BaseAgent
from ..types import AgentResponse, AgentType, UserRequest


class SEOAgent(BaseAgent):
    """Handles: keyword research, meta tags, sitemap suggestions, structure."""

    agent_type = AgentType.SEO

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        # Placeholder: in production, would call LLM with SEO-specific prompt
        return AgentResponse(
            agent_type=self.agent_type,
            content=f"[SEO Agent] Verarbeitung der Anfrage: {request.message[:100]}...\n\n"
            "Empfehlung: Keyword-Recherche und Meta-Tags optimieren.",
            metadata={"status": "pending_llm"},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Keyword research",
            "Meta tag suggestions",
            "Sitemap structure",
            "On-page optimization",
            "Search intent analysis",
        ]
