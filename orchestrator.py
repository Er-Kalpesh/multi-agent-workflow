import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Initialize the Gemini client
# Ensure GEMINI_API_KEY is set in your .env file
client = genai.Client()

def call_agent(client: genai.Client, role_prompt: str, user_prompt: str) -> str:
    """Helper function to call a Gemini agent with a specific role."""
    print(f"--- Calling Agent ---")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=role_prompt,
                temperature=0.4,
            ),
        )
        return response.text
    except Exception as e:
        print(f"Error calling agent: {e}")
        return f"Error: {e}"

def run_workflow(problem_description: str):
    print(f"Starting Multi-Agent Workflow for problem:\n{problem_description}\n")

    # 1. Researcher Phase
    researcher_sys_prompt = (
        "You are an expert AI Researcher. Your task is to analyze coding problems, "
        "identify the best algorithms, libraries, and design patterns to solve them. "
        "Provide a clear, high-level plan and point out potential pitfalls."
    )
    print(">> Phase 1: Research")
    research_plan = call_agent(client, researcher_sys_prompt, problem_description)
    print(f"Researcher Output:\n{research_plan}\n")

    # 2. Coder Phase
    coder_sys_prompt = (
        "You are an expert AI Software Engineer. Your task is to write clean, "
        "efficient, and well-documented Python code based on the provided research plan "
        "and problem description. Only output the code and essential explanations."
    )
    coder_input = (
        f"Problem: {problem_description}\n\n"
        f"Research Plan: {research_plan}\n\n"
        "Please implement the solution."
    )
    print(">> Phase 2: Coding")
    code_solution = call_agent(client, coder_sys_prompt, coder_input)
    print(f"Coder Output:\n{code_solution}\n")

    # 3. Reviewer Phase
    reviewer_sys_prompt = (
        "You are an expert AI Code Reviewer. Your task is to critically analyze the "
        "provided code for correctness, performance, security, and adherence to best practices. "
        "Provide specific feedback, suggest improvements, and state whether the code is approved."
    )
    reviewer_input = (
        f"Problem: {problem_description}\n\n"
        f"Code Implementation: {code_solution}\n\n"
        "Please review this code."
    )
    print(">> Phase 3: Review")
    review_feedback = call_agent(client, reviewer_sys_prompt, reviewer_input)
    print(f"Reviewer Output:\n{review_feedback}\n")

    print("=== Workflow Complete ===")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem = " ".join(sys.argv[1:])
    else:
        problem = "Write a Python function to find the longest palindromic substring in a given string. Include comprehensive unit tests."
    
    run_workflow(problem)
