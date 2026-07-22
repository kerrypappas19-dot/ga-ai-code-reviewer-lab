# ======================================================
# GA Micro-Lab: Automated AI Code Reviewer (Python)
# Target: Instant feedback loop for remote programming labs
# ======================================================

import os

REVIEW_SYSTEM_PROMPT = """
You are an expert programming mentor. Review the provided student code snippet.
Rules:
1. Identify any syntax bugs or security vulnerabilities.
2. Provide feedback in under 40 words.
3. Maintain an encouraging, constructive tone.
"""

def review_student_code(student_code, system_prompt):
    payload = {
        "system": system_prompt,
        "code_input": student_code,
        "max_tokens": 60
    }
    print(f"[GitHub Integration]: Fetching snippet... Analyzing payload ({payload['max_tokens']} max tokens).")
    return "Feedback: Great job using a function! Watch out for missing exception handling on line 4."

sample_code = """
def calc(x, y):
    return x + y
"""
print(review_student_code(sample_code, REVIEW_SYSTEM_PROMPT))
