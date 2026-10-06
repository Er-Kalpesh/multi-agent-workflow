# Multi-Agent Workflow Engine

Welcome to the **Multi-Agent Workflow Engine**, created by **Er-Kalpesh**.

This project demonstrates a sophisticated multi-agent orchestration system using the `google-genai` SDK. It coordinates three distinct AI subagents—a Researcher, a Coder, and a Reviewer—to autonomously solve complex coding problems in a multi-step workflow.

## Features

- **Researcher Agent**: Gathers context, explores approaches, and identifies the best tools/libraries for the problem.
- **Coder Agent**: Implements the solution based on the Researcher's findings, ensuring clean and efficient code.
- **Reviewer Agent**: Critiques the code, checks for edge cases, and provides feedback or validation.
- **Orchestrator**: Seamlessly manages the state and flow of information between the subagents using the Gemini API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Er-Kalpesh/multi-agent-workflow-engine.git
   cd multi-agent-workflow-engine
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Copy `.env.example` to `.env` and add your Gemini API key:
   ```bash
   cp .env.example .env
   ```

## Usage

Run the orchestrator script to start the multi-agent workflow:
```bash
python orchestrator.py
```

## About the Author

This project is part of the portfolio of **Er-Kalpesh**, showcasing advanced AI agent orchestration and workflow engineering using modern generative AI SDKs.

## License

This project is open-source and available under the MIT License.
