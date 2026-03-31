import os
from groq import Groq

def init_ai():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return Groq(api_key=api_key)

def generate_summary(client, metadata):
    prompt = f"""You are helping a beginner understand a GitHub repo.
Explain what this project does in plain English.
Include what the project does, who it's for, why it exists, and what problem it solves.
Aim for 5-6 sentences. Keep it beginner friendly with no jargon.

Project: {metadata['repo']}
Description: {metadata['description']}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_contribution_guide(client, metadata, files):
    file_list = ", ".join([f["name"] for f in files]) if files else "none"
    prompt = f"""You are a mentor helping a beginner contribute to open source.
Write a simple 3-step guide to contribute to this project.

Project: {metadata['repo']}
Key Files: {file_list}

Keep it simple and encouraging.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
