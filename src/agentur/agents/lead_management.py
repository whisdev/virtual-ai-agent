"""Lead Management agent — qualification, follow-up, CRM."""

from ..base_agent import BaseAgent
from ..prompts import AGENT_PROMPTS
from ..types import AgentResponse, AgentType, UserRequest


class LeadManagementAgent(BaseAgent):
    """Handles: lead scoring, email sequences, CRM updates, qualification."""

    agent_type = AgentType.LEAD_MANAGEMENT
    _prompt_key = "lead_management"

    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        lang = context.get("lang", "de")
        content = self._generate(AGENT_PROMPTS["lead_management"], request.message)
        return AgentResponse(
            agent_type=self.agent_type,
            content=content,
            metadata={"lang": lang},
        )

    def get_capabilities(self) -> list[str]:
        return [
            "Lead scoring",
            "Email sequences",
            "CRM updates",
            "Qualification criteria",
            "Follow-up suggestions",
        ]
