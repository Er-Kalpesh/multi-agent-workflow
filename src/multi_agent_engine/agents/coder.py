from .base_agent import BaseAgent
from ..state import WorkflowState
from ..utils.logger import get_logger
from google.genai import types

logger = get_logger(__name__)

class CoderAgent(BaseAgent):
    @property
    def system_prompt(self) -> str:
        return (
            "You are an expert Principal AI Software Engineer. Your task is to write clean, "
            "production-ready, and well-documented code based on the provided research plan. "
            "Follow best practices, include type hints, and ensure modularity. "
            "Output only the code and essential explanations."
        )

    def execute(self, state: WorkflowState) -> WorkflowState:
        logger.info("[bold cyan]Coder Agent[/] is generating the solution...")
        
        prompt = (
            f"Problem: {state.problem_description}\n\n"
            f"Research Plan: {state.research_plan}\n\n"
            "Please implement the solution."
        )
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt,
                    temperature=0.2,
                ),
            )
            state.code_solution = response.text
            logger.info("[bold green]Coder Agent[/] completed the coding phase.")
        except Exception as e:
            logger.error(f"[bold red]Coder Agent[/] encountered an error: {e}")
            state.code_solution = f"Error during coding phase: {e}"
            
        return state
