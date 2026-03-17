"""Entry point — run the agent system."""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from .orchestrator import Orchestrator
from .types import UserRequest


def main() -> None:
    """Run a demo request through the orchestrator."""
    orchestrator = Orchestrator()

    # Demo request
    request = UserRequest(
        message="Erstelle einen Blog-Beitrag über SEO für den deutschen Markt und optimiere die Meta-Tags.",
        session_id="demo-001",
        context={"lang": os.getenv("DEFAULT_LANG", "de")},
    )

    print("User request:", request.message)
    print()

    decision = orchestrator.route(request)
    print("Orchestrator decision:")
    print(f"  Target agents: {[a.value for a in decision.target_agents]}")
    print(f"  Reasoning: {decision.reasoning}")
    print()

    results = orchestrator.execute(request, decision)
    print("Agent responses:")
    for r in results:
        print(f"  [{r.agent_type.value}] {r.content[:150]}...")
        print()


if __name__ == "__main__":
    main()
