# Multi-Agent Workflow Engine

Welcome to the **Multi-Agent Workflow Engine**, created by **Er-Kalpesh**.

This project demonstrates a production-grade, multi-agent orchestration system using the `google-genai` SDK and `gemini-2.5-flash`. It coordinates three distinct AI subagents—a Researcher, a Coder, and a Reviewer—to autonomously solve complex coding problems in a multi-step workflow.

## 🌟 Enterprise Architecture

The engine is built with a modular, scalable architecture reflecting Senior AI Engineer standards:

- **State Management**: Uses `Pydantic` models for robust type-safe state transitions between agents.
- **Structured Outputs**: The Reviewer agent utilizes Gemini's Structured Outputs (JSON Schema) to guarantee reliable, parsable feedback.
- **Feedback Loops**: Features an iterative workflow orchestrator where the code is recursively improved based on the reviewer's critiques until approval or a maximum iteration limit is reached.
- **Rich Logging**: Uses the `Rich` library to provide beautiful, color-coded, and traceable terminal output.
- **Object-Oriented Design**: Agents inherit from a common abstract base class, making the system highly extensible for adding new agents (e.g., a Tester Agent, a Deployment Agent).

## 🛠️ Project Structure

```
.
├── src/
│   └── multi_agent_engine/
│       ├── agents/
│       │   ├── base_agent.py      # Abstract Base Agent
│       │   ├── coder.py           # Code Generation Agent
│       │   ├── researcher.py      # Research & Planning Agent
│       │   └── reviewer.py        # Code Review & Validation Agent (Structured Output)
│       ├── core/
│       │   └── orchestrator.py    # State machine and feedback loop coordinator
│       ├── utils/
│       │   └── logger.py          # Rich terminal logger
│       └── state.py               # Pydantic WorkflowState models
├── tests/
│   └── test_agents.py             # Pytest unit tests
├── main.py                        # Entry point
├── pyproject.toml                 # Package definition
└── requirements.txt               # Dependencies
```

## 🚀 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Er-Kalpesh/multi-agent-workflow-engine.git
   cd multi-agent-workflow-engine
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -e .
   ```

3. Set up the environment variables:
   Copy `.env.example` to `.env` and add your Gemini API key:
   ```bash
   cp .env.example .env
   # Edit .env and set GEMINI_API_KEY
   ```

4. Run the workflow:
   ```bash
   python main.py "Write a Python function to solve the Traveling Salesperson Problem (TSP) using dynamic programming with bitmasking. Include type hints and comprehensive unit tests."
   ```

## 🧪 Testing

Run the test suite using `pytest`:
```bash
pytest
```

## 👨‍💻 About the Author

This project is part of the portfolio of **Er-Kalpesh**, showcasing advanced AI agent orchestration, state management, and workflow engineering using modern generative AI SDKs.

## 📄 License

This project is open-source and available under the MIT License.
