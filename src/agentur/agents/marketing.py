"""Marketing agent — campaigns, messaging, audience targeting."""

from ..base_agent import BaseAgent
from ..prompts import AGENT_PROMPTS
from ..types import AgentResponse, AgentType, UserRequest


class MarketingAgent(BaseAgent):
    """Handles: ad copy, A/B ideas, channel strategy, campaign planning."""

    agent_type = AgentType.MARKETING
    _prompt_key = "marketing"

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        lang = context.get("lang", "de")
        content = self._generate(AGENT_PROMPTS["marketing"], request.message)
        return AgentResponse(
            agent_type=self.agent_type,
            content=content,
            metadata={"lang": lang},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Ad copy generation",
            "A/B test ideas",
            "Channel strategy",
            "Campaign planning",
            "Audience targeting",
        ]
