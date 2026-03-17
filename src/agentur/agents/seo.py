"""SEO agent — search visibility, keywords, structure."""

from ..base_agent import BaseAgent
from ..prompts import AGENT_PROMPTS
from ..types import AgentResponse, AgentType, UserRequest


class SEOAgent(BaseAgent):
    """Handles: keyword research, meta tags, sitemap suggestions, structure."""

    agent_type = AgentType.SEO
    _prompt_key = "seo"

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        lang = context.get("lang", "de")
        prior = context.get("previous_responses", [])

        user_msg = request.message
        if prior:
            prior_text = "\n".join(
                f"- {r.get('agent_type', '?')}: {r.get('content', '')[:300]}..."
                for r in prior
            )
            user_msg = f"Kontext (z.B. von Content-Agent):\n{prior_text}\n\nSEO-Anfrage:\n{request.message}"

        content = self._generate(AGENT_PROMPTS["seo"], user_msg)
        return AgentResponse(
            agent_type=self.agent_type,
            content=content,
            metadata={"lang": lang},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Keyword research",
            "Meta tag suggestions",
            "Sitemap structure",
            "On-page optimization",
            "Search intent analysis",
        ]
