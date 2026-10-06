import time
from ..state import WorkflowState
from ..agents import ResearcherAgent, CoderAgent, ReviewerAgent
from ..utils.logger import get_logger

logger = get_logger(__name__)

class WorkflowOrchestrator:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.researcher = ResearcherAgent(model_name=model_name)
        self.coder = CoderAgent(model_name=model_name)
        self.reviewer = ReviewerAgent(model_name=model_name)

    def run(self, problem_description: str) -> WorkflowState:
        logger.info("\n[bold magenta]=== Starting Multi-Agent Workflow ===[/]")
        logger.info(f"Problem: {problem_description}\n")

        state = WorkflowState(problem_description=problem_description)

        # Step 1: Research
        state = self.researcher.execute(state)

        # Step 2 & 3: Code and Review (with iteration)
        while state.iteration_count < state.max_iterations:
            state.iteration_count += 1
            logger.info(f"\n[bold blue]--- Iteration {state.iteration_count}/{state.max_iterations} ---[/]")
            
            # Code Phase
            state = self.coder.execute(state)
            
            # Review Phase
            state = self.reviewer.execute(state)
            
            if state.review_feedback and state.review_feedback.is_approved:
                logger.info("\n[bold green]Success: Code approved by Reviewer![/]")
                break
            else:
                logger.info("\n[bold yellow]Reviewer requested changes. Updating problem context for next iteration.[/]")
                # Append feedback to the research plan or problem description for the coder's next try
                state.research_plan += f"\n\n--- Reviewer Feedback (Iteration {state.iteration_count}) ---\n"
                state.research_plan += state.review_feedback.feedback_notes if state.review_feedback else "Unknown error."
                time.sleep(1) # Small delay to avoid API rate limits

        if state.review_feedback and not state.review_feedback.is_approved:
            logger.info(f"\n[bold red]Failed: Workflow reached max iterations ({state.max_iterations}) without approval.[/]")

        logger.info("\n[bold magenta]=== Workflow Complete ===[/]")
        return state
