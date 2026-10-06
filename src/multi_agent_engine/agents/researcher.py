from .base_agent import BaseAgent
from ..state import WorkflowState
from ..utils.logger import get_logger
from google.genai import types

logger = get_logger(__name__)

class ResearcherAgent(BaseAgent):
    @property
    def system_prompt(self) -> str:
        return (
            "You are a Staff-level AI Researcher. Your task is to analyze coding problems, "
            "identify optimal algorithms, libraries, design patterns, and edge cases. "
            "Provide a comprehensive, high-level technical plan and highlight potential pitfalls."
        )

    def execute(self, state: WorkflowState) -> WorkflowState:
        logger.info("[bold cyan]Researcher Agent[/] is analyzing the problem...")
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=state.problem_description,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt,
                    temperature=0.4,
                ),
            )
            state.research_plan = response.text
            logger.info("[bold green]Researcher Agent[/] completed the analysis.")
        except Exception as e:
            logger.error(f"[bold red]Researcher Agent[/] encountered an error: {e}")
            state.research_plan = f"Error during research phase: {e}"
            
        return state
