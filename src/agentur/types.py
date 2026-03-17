"""Shared types for the agent system."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentType(str, Enum):
    """Specialist agent types."""

    MARKETING = "marketing"
    SEO = "seo"
    CONTENT = "content"
    LEAD_MANAGEMENT = "lead_management"


@dataclass
class UserRequest:
    """Incoming user request."""

    message: str
    session_id: str | None = None
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentResponse:
    """Response from a specialist agent."""

    agent_type: AgentType
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestratorDecision:
    """Orchestrator's routing decision."""

    target_agents: list[AgentType]
    reasoning: str
    workflow_steps: list[str] = field(default_factory=list)
