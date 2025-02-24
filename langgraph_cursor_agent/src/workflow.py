from typing import Dict, TypedDict, Callable, Union
from langgraph.graph import Graph, StateGraph
from agents.pdf_reader_agent import PDFReaderAgent
from agents.translation_agent import TranslationAgent
from agents.presentation_designer_agent import PresentationDesignerAgent
from agents.review_agent import ReviewAgent
from agents.improvement_agent import ImprovementAgent


class AgentState(TypedDict):
    pdf_content: Dict
    translated_content: Dict
    presentation: Dict
    review_feedback: Dict
    status: str
    current_agent: str
    messages: list
    errors: list


def create_workflow() -> Graph:
    """Create the LangGraph workflow for presentation generation"""

    # Initialize agents
    pdf_reader = PDFReaderAgent()
    translator = TranslationAgent()
    designer = PresentationDesignerAgent()
    reviewer = ReviewAgent()
    improver = ImprovementAgent()

    # Create workflow graph
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("pdf_reader", pdf_reader.process)
    workflow.add_node("translator", translator.process)
    workflow.add_node("designer", designer.process)
    workflow.add_node("reviewer", reviewer.process)
    workflow.add_node("improver", improver.process)
    # End node that returns the final state
    workflow.add_node("end", lambda x: x)

    # Define conditional edges
    workflow.add_conditional_edges(
        "reviewer",
        # Function that determines which node to go to next
        lambda x: "improver" if x.get("review_feedback", {}).get(
            "accuracy_score", 1.0) < 0.8 else "end",
        # Map condition results to nodes
        {
            "improver": "improver",
            "end": "end"
        }
    )

    # Connect other nodes
    workflow.add_edge("pdf_reader", "translator")
    workflow.add_edge("translator", "designer")
    workflow.add_edge("designer", "reviewer")
    workflow.add_edge("improver", "reviewer")

    # Set entry point
    workflow.set_entry_point("pdf_reader")

    # Compile workflow
    app = workflow.compile()

    return app


def create_initial_state() -> AgentState:
    """Create initial state for the workflow"""
    return AgentState(
        pdf_content={},
        translated_content={},
        presentation={},
        review_feedback={},
        status="Starting",
        current_agent="PDF Reader Agent",
        messages=[],
        errors=[]
    )
