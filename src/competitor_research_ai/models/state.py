"""State schema for the research report generation workflow.

Using TypedDict for lightweight state management with LangGraph.
"""
from typing import Annotated, TypedDict, Literal
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    """Main state schema for the research workflow.
    
    This uses TypedDict for optimal performance with LangGraph[web:58][web:59][web:62].
    All state fields are tracked across the graph execution.
    """
    
    # Messages for conversational context
    messages: Annotated[list[AnyMessage], add_messages]
    
    # Research Query & Planning
    original_query: str  # User's initial request
    refined_query: str  # Human-approved query after refinement
    research_plan: list[str]  # List of research questions to answer
    
    # Research Data
    search_results: list[dict]  # Raw search results from Tavily
    research_findings: str  # Synthesized findings from research
    
    # Report Generation
    report_outline: list[str]  # Report section headings
    report_content: str  # Final report content
    report_status: Literal["draft", "review", "final"]  # Report state
    
    # Workflow Control
    current_step: str  # Current node in the workflow
    human_feedback: str | None  # Feedback from human review
    requires_approval: bool  # Flag for human-in-the-loop
    iteration_count: int  # Track iterations for safety limits
    
    # Metadata
    competitor_name: str | None  # For competitor analysis use case
    error_message: str | None  # Error tracking


class QueryRefinementInput(TypedDict):
    """Input schema for query refinement human approval."""
    original_query: str
    suggested_refinements: list[str]
    recommended_query: str


class HumanFeedback(TypedDict):
    """Schema for human feedback at checkpoints."""
    approved: bool
    feedback: str | None
    modified_input: str | None  # Human's edited version
