from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AgentFeedback(BaseModel):
    is_approved: bool = Field(description="Whether the code is approved.")
    feedback_notes: str = Field(description="Detailed feedback or suggested improvements.")

class WorkflowState(BaseModel):
    problem_description: str
    research_plan: Optional[str] = None
    code_solution: Optional[str] = None
    review_feedback: Optional[AgentFeedback] = None
    iteration_count: int = 0
    max_iterations: int = 3
    metadata: Dict[str, Any] = Field(default_factory=dict)
