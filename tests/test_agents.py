import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Set a dummy API key for testing
os.environ["GEMINI_API_KEY"] = "dummy_key_for_testing"

from multi_agent_engine.state import WorkflowState
from multi_agent_engine.agents.base_agent import BaseAgent

class MockAgent(BaseAgent):
    def __init__(self, model_name: str = "mock-model"):
        self.model_name = model_name
        # Skip creating a real genai.Client
        
    @property
    def system_prompt(self) -> str:
        return "Mock Prompt"
        
    def execute(self, state: WorkflowState) -> WorkflowState:
        state.metadata["mock_executed"] = True
        return state

def test_workflow_state_initialization():
    state = WorkflowState(problem_description="Test Problem")
    assert state.problem_description == "Test Problem"
    assert state.iteration_count == 0
    assert state.research_plan is None

def test_mock_agent_execution():
    state = WorkflowState(problem_description="Test Problem")
    agent = MockAgent(model_name="mock-model")
    state = agent.execute(state)
    
    assert state.metadata.get("mock_executed") is True
