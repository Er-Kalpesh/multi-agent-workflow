from abc import ABC, abstractmethod
from typing import Any
from google import genai
import os

class BaseAgent(ABC):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.model_name = model_name
        self.client = genai.Client()
        
    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """Return the system prompt for the agent."""
        pass
        
    @abstractmethod
    def execute(self, state: Any) -> Any:
        """Execute the agent's primary task given the workflow state."""
        pass
