import sys
import os
from dotenv import load_dotenv

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from multi_agent_engine.core.orchestrator import WorkflowOrchestrator
from multi_agent_engine.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    load_dotenv()
    
    if not os.getenv("GEMINI_API_KEY"):
        logger.error("[bold red]GEMINI_API_KEY environment variable is not set. Please set it in your .env file.[/]")
        sys.exit(1)

    # Use gemini-2.5-flash as the default model
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    
    orchestrator = WorkflowOrchestrator(model_name=model_name)
    
    if len(sys.argv) > 1:
        problem = " ".join(sys.argv[1:])
    else:
        problem = (
            "Write a Python function to solve the Traveling Salesperson Problem (TSP) "
            "using dynamic programming with bitmasking. Include type hints and comprehensive unit tests."
        )
        
    try:
        final_state = orchestrator.run(problem)
        
        print("\n" + "="*50)
        print("FINAL SOLUTION")
        print("="*50)
        print(final_state.code_solution)
        
        print("\n" + "="*50)
        print("REVIEWER FEEDBACK")
        print("="*50)
        print(f"Approved: {final_state.review_feedback.is_approved if final_state.review_feedback else False}")
        print(final_state.review_feedback.feedback_notes if final_state.review_feedback else "No feedback.")
        
    except KeyboardInterrupt:
        logger.info("\n[bold yellow]Workflow interrupted by user.[/]")
        sys.exit(0)

if __name__ == "__main__":
    main()
