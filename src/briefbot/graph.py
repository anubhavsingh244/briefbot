"""LangGraph workflow. This is a one-node stub: replace it with the real graph.

Target shape (see README):
    planner -> researcher x N (Send fan-out) -> synthesizer -> writer -> critic
    critic --fail--> planner (max 2 loops) | --pass--> human review (interrupt)
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class BriefState(TypedDict, total=False):
    topic: str
    draft: str


def write_stub(state: BriefState) -> BriefState:
    # TODO: replace with planner / researcher / writer / critic nodes.
    return {"draft": f"# Brief: {state['topic']}\n\n(stub draft, no LLM call yet)"}


def build_graph():
    g = StateGraph(BriefState)
    g.add_node("write_stub", write_stub)
    g.add_edge(START, "write_stub")
    g.add_edge("write_stub", END)
    return g.compile()
