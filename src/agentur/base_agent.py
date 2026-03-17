"""Base agent interface."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .types import AgentResponse, AgentType, UserRequest

if TYPE_CHECKING:
    from .llm import LLMClient


class BaseAgent(ABC):
    """Base class for specialist agents."""

    agent_type: AgentType
    _prompt_key: str = ""

    def __init__(self, llm: "LLMClient | None" = None) -> None:
        self._llm = llm

    @abstractmethod
    def handle(self, request: UserRequest, context: dict) -> AgentResponse:
        """Process a request and return a response."""
        ...

    @abstractmethod
    def get_capabilities(self) -> list[str]:
        """Return list of tasks this agent can handle."""
        ...

    def _generate(self, system_prompt: str, user_message: str) -> str:
        """Call LLM or return fallback."""
        if self._llm:
            return self._llm.complete(system_prompt, user_message)
        return self._fallback_response(user_message)

    def _fallback_response(self, user_message: str) -> str:
        """Return when LLM is not configured."""
        return (
            f"[{self.agent_type.value}] Kein LLM konfiguriert. "
            f"Bitte LITELLM_MODEL und API-Key setzen (z.B. openai/gpt-4o). "
            f"Anfrage: {user_message[:80]}..."
        )
