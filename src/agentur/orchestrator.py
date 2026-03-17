"""Central orchestrator agent — routes requests and coordinates workflow."""

from .agents import get_agents
from .types import AgentType, OrchestratorDecision, UserRequest


class Orchestrator:
    """
    Central coordinator that:
    - Receives user requests
    - Decides which specialist agent(s) to delegate to
    - Aggregates results
    - Manages workflow state
    """

    def __init__(self) -> None:
        self._agents = get_agents()

    def route(self, request: UserRequest) -> OrchestratorDecision:
        """
        Analyze the request and decide which agent(s) should handle it.
        In production, this would use an LLM for intelligent routing.
        """
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
            target_agents = [AgentType.CONTENT]  # Default fallback

        return OrchestratorDecision(
            target_agents=target_agents,
            reasoning=f"Routed to {[a.value for a in target_agents]} based on request content",
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
