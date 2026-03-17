"""Entry point — run the agent system."""

import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from .llm import get_llm_client
from .orchestrator import Orchestrator
from .types import UserRequest


def _print_separator(char: str = "─", width: int = 70) -> None:
    print(char * width)


def _print_response(agent_type: str, content: str) -> None:
    _print_separator()
    print(f"  [{agent_type.upper()}]")
    _print_separator("─", 70)
    print(content.strip())
    print()


def run_single(request: UserRequest, orchestrator: Orchestrator) -> None:
    """Process one request and print full results."""
    print()
    _print_separator("═")
    print("  ANFRAGE")
    _print_separator("═")
    print(f"  {request.message}")
    print()

    decision = orchestrator.route(request)
    print("  Routing:", ", ".join(a.value for a in decision.target_agents))
    print("  Begründung:", decision.reasoning)
    print()

    results = orchestrator.execute(request, decision)

    _print_separator("═")
    print("  ERGEBNISSE")
    _print_separator("═")
    for r in results:
        _print_response(r.agent_type.value, r.content)


def run_interactive(orchestrator: Orchestrator) -> None:
    """Interactive mode: user types requests, gets full responses."""
    print()
    _print_separator("═")
    print("  Virtuelle Agentur — Interaktiver Modus")
    _print_separator("═")
    print("  Gib eine Anfrage ein (z.B. Blog-Beitrag, SEO, Marketing).")
    print("  'quit' oder 'exit' zum Beenden.")
    _print_separator()
    print()

    session_id = "interactive-001"
    lang = os.getenv("DEFAULT_LANG", "de")

    while True:
        try:
            line = input("  Anfrage> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Auf Wiedersehen.")
            break

        if not line:
            continue
        if line.lower() in ("quit", "exit", "q"):
            print("  Auf Wiedersehen.")
            break

        request = UserRequest(
            message=line,
            session_id=session_id,
            context={"lang": lang},
        )
        run_single(request, orchestrator)


def main() -> None:
    """Run demo or interactive mode."""
    llm = get_llm_client()
    if not llm:
        print(
            "Hinweis: Kein LLM konfiguriert. Setze LITELLM_MODEL (z.B. openai/gpt-4o) und API-Key.",
            file=sys.stderr,
        )
        print("  Fallback: Keyword-Routing und Platzhalter-Antworten.", file=sys.stderr)
        print(file=sys.stderr)

    orchestrator = Orchestrator(llm=llm)

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive(orchestrator)
        return

    # Demo request
    request = UserRequest(
        message="Erstelle einen Blog-Beitrag über SEO für den deutschen Markt und optimiere die Meta-Tags.",
        session_id="demo-001",
        context={"lang": os.getenv("DEFAULT_LANG", "de")},
    )
    run_single(request, orchestrator)


if __name__ == "__main__":
    main()
