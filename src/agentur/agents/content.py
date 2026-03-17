"""Content Creation agent — blog posts, social, landing pages."""

from ..base_agent import BaseAgent
from ..types import AgentResponse, AgentType, UserRequest


class ContentAgent(BaseAgent):
    """Handles: articles, captions, product descriptions, landing pages."""

    agent_type = AgentType.CONTENT

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        # Placeholder: in production, would call LLM with content-specific prompt
        return AgentResponse(
            agent_type=self.agent_type,
            content=f"[Content Agent] Verarbeitung der Anfrage: {request.message[:100]}...\n\n"
            "Empfehlung: Blog-Beitrag oder Social-Media-Content erstellen.",
            metadata={"status": "pending_llm"},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Blog posts",
            "Social media captions",
            "Product descriptions",
            "Landing page copy",
            "Email content",
        ]
