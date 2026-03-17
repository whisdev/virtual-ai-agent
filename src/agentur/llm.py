"""LLM client via LiteLLM — unified gateway for OpenAI, Anthropic, Ollama, etc."""

import os
from typing import Protocol


class LLMClient(Protocol):
    """Protocol for LLM clients."""

    def complete(self, system_prompt: str, user_message: str) -> str:
        """Generate completion. Returns text or raises on error."""
        ...


def get_llm_client() -> "LiteLLMClient | None":
    """Return configured LiteLLM client, or None if not configured."""
    model = os.getenv("LITELLM_MODEL", "").strip()
    if not model:
        return None

    # LiteLLM reads API keys from env (OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.)
    # For ollama/* no key needed
    if model.startswith("ollama/"):
        return LiteLLMClient(model=model)

    provider = model.split("/")[0] if "/" in model else "openai"
    key_var = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY"}.get(
        provider
    )
    if key_var and not os.getenv(key_var):
        return None

    return LiteLLMClient(model=model)


class LiteLLMClient:
    """Unified LLM client using LiteLLM as model gateway."""

    def __init__(self, model: str) -> None:
        self._model = model

    def complete(self, system_prompt: str, user_message: str) -> str:
        from litellm import completion

        response = completion(
            model=self._model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content or ""
