"""Specialist agents."""

from ..base_agent import BaseAgent
from ..llm import get_llm_client
from ..types import AgentType
from .content import ContentAgent
from .lead_management import LeadManagementAgent
from .marketing import MarketingAgent
from .seo import SEOAgent


def get_agents(llm=None):
    """Return registry of specialist agents. Pass llm for real LLM calls."""
    if llm is None:
        llm = get_llm_client()
    agents: dict[AgentType, BaseAgent] = {
        AgentType.MARKETING: MarketingAgent(llm=llm),
        AgentType.SEO: SEOAgent(llm=llm),
        AgentType.CONTENT: ContentAgent(llm=llm),
        AgentType.LEAD_MANAGEMENT: LeadManagementAgent(llm=llm),
    }
    return agents
