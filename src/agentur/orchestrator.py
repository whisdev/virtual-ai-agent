"""Central orchestrator agent — routes requests and coordinates workflow."""

import json

from .agents import get_agents
from .llm import get_llm_client
from .types import AgentType, OrchestratorDecision, UserRequest


class Orchestrator:
    """
    Central coordinator that:
    - Receives user requests
    - Decides which specialist agent(s) to delegate to
    - Aggregates results
    - Manages workflow state
    """

    def __init__(self, llm=None) -> None:
        self._llm = llm or get_llm_client()
        self._agents = get_agents(llm=self._llm)

    def route(self, request: UserRequest) -> OrchestratorDecision:
        """Analyze the request and decide which agent(s) should handle it."""
        if self._llm:
            try:
                from .prompts import ORCHESTRATOR_ROUTING_PROMPT

                raw = self._llm.complete(
                    ORCHESTRATOR_ROUTING_PROMPT,
                    request.message,
                )
                # Extract JSON from response
                start, end = raw.find("{"), raw.rfind("}") + 1
                if start >= 0 and end > start:
                    data = json.loads(raw[start:end])
                    agent_names = data.get("agents", [])
                    reasoning = data.get("reasoning", "")
                    target_agents = [
                        AgentType(a) for a in agent_names if a in [e.value for e in AgentType]
                    ]
                    if target_agents:
                        return OrchestratorDecision(
                            target_agents=target_agents,
                            reasoning=reasoning or f"LLM routed to {agent_names}",
                            workflow_steps=[f"Delegate to {a.value}" for a in target_agents],
                        )
            except (json.JSONDecodeError, ValueError, KeyError):
                pass

        # Fallback: keyword-based routing
        return self._route_by_keywords(request)

    def _route_by_keywords(self, request: UserRequest) -> OrchestratorDecision:
        """Keyword-based routing when LLM is unavailable."""
        message_lower = request.message.lower()
        target_agents: list[AgentType] = []
        keywords: dict[AgentType, list[str]] = {
            AgentType.MARKETING: [
                "kampagne", "werbung", "ad", "marketing", "zielgruppe",
                "campaign", "ad copy", "channel strategy",
            ],
            AgentType.SEO: [
                "seo", "keyword", "suchmaschine", "meta", "sitemap",
                "search", "ranking", "meta tags",
            ],
            AgentType.CONTENT: [
                "blog", "beitrag", "text", "content", "landing page",
                "article", "post", "beschreibung", "caption",
            ],
            AgentType.LEAD_MANAGEMENT: [
                "lead", "kunde", "qualifizierung", "follow-up", "crm",
                "lead scoring", "email sequence",
            ],
        }

        for agent_type, words in keywords.items():
            if any(w in message_lower for w in words):
                target_agents.append(agent_type)

        if not target_agents:
            target_agents = [AgentType.CONTENT]

        return OrchestratorDecision(
            target_agents=target_agents,
            reasoning=f"Keyword-routing zu {[a.value for a in target_agents]}",
            workflow_steps=[f"Delegate to {a.value}" for a in target_agents],
        )

    def execute(self, request: UserRequest, decision: OrchestratorDecision) -> list:
        """Delegate to specialist agents and collect responses."""
        results = []
        context = request.context.copy()

        for agent_type in decision.target_agents:
            agent = self._agents.get(agent_type)
            if agent:
                response = agent.handle(request, context)
                results.append(response)
                context["previous_responses"] = [
                    {"agent_type": r.agent_type.value, "content": r.content}
                    for r in results
                ]
        return results
