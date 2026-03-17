"""Base agent interface."""

from abc import ABC, abstractmethod

from .types import AgentResponse, AgentType, UserRequest


class BaseAgent(ABC):
    """Base class for specialist agents."""

    agent_type: AgentType

    @abstractmethod
    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        """Process a request and return a response."""
        ...

    @abstractmethod
    def get_capabilities(self) -> list[str]:
        """Return list of tasks this agent can handle."""
        ...
