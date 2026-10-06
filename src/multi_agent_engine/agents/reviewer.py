from .base_agent import BaseAgent
from ..state import WorkflowState, AgentFeedback
from ..utils.logger import get_logger
from google.genai import types

logger = get_logger(__name__)

class ReviewerAgent(BaseAgent):
    @property
    def system_prompt(self) -> str:
        return (
            "You are a strict, Senior Staff Code Reviewer. Your task is to critically analyze "
            "code for correctness, performance, security, and enterprise standards. "
            "Provide detailed feedback, point out any flaws, and state clearly whether "
            "the code is approved or needs revision."
        )

    def execute(self, state: WorkflowState) -> WorkflowState:
        logger.info("[bold cyan]Reviewer Agent[/] is reviewing the code...")
        
        prompt = (
            f"Problem: {state.problem_description}\n\n"
            f"Code Implementation: {state.code_solution}\n\n"
            "Please review this code and provide structured feedback."
        )
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt,
                    temperature=0.1,
                    response_mime_type="application/json",
                    response_schema=AgentFeedback,
                ),
            )
            # The SDK parses the JSON response into a dictionary if schema is provided.
            # But just in case, we'll construct the Pydantic model.
            import json
            feedback_data = json.loads(response.text)
            state.review_feedback = AgentFeedback(**feedback_data)
            
            status_color = "bold green" if state.review_feedback.is_approved else "bold yellow"
            logger.info(f"[{status_color}]Reviewer Agent[/] finished review. Approved: {state.review_feedback.is_approved}")
        except Exception as e:
            logger.error(f"[bold red]Reviewer Agent[/] encountered an error: {e}")
            state.review_feedback = AgentFeedback(is_approved=False, feedback_notes=f"Error during review phase: {e}")
            
        return state
