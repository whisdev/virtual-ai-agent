"""Content Creation agent — blog posts, social, landing pages."""

from ..base_agent import BaseAgent
from ..prompts import AGENT_PROMPTS
from ..types import AgentResponse, AgentType, UserRequest


class ContentAgent(BaseAgent):
    """Handles: articles, captions, product descriptions, landing pages."""

    agent_type = AgentType.CONTENT
    _prompt_key = "content"

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        lang = context.get("lang", "de")
        prior = context.get("previous_responses", [])

        user_msg = request.message
        if prior:
            prior_text = "\n".join(
                f"- {r.get('agent_type', '?')}: {r.get('content', '')[:200]}..."
                for r in prior
            )
            user_msg = f"Kontext von anderen Agenten:\n{prior_text}\n\nHauptanfrage:\n{request.message}"

        content = self._generate(AGENT_PROMPTS["content"], user_msg)
        return AgentResponse(
            agent_type=self.agent_type,
            content=content,
            metadata={"lang": lang},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Blog posts",
            "Social media captions",
            "Product descriptions",
            "Landing page copy",
            "Email content",
        ]
