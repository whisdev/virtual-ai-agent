"""Specialist agents."""

from ..base_agent import BaseAgent
from ..types import AgentType
from .content import ContentAgent
from .lead_management import LeadManagementAgent
from .marketing import MarketingAgent
from .seo import SEOAgent


def get_agents() -> dict[AgentType, BaseAgent]:
    """Return registry of specialist agents."""
    agents: dict[AgentType, BaseAgent] = {
        AgentType.MARKETING: MarketingAgent(),
        AgentType.SEO: SEOAgent(),
        AgentType.CONTENT: ContentAgent(),
        AgentType.LEAD_MANAGEMENT: LeadManagementAgent(),
    }
    return agents
