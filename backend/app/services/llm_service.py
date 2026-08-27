import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env")


client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_resume(resume_text: str, job_description: str) -> dict:

    prompt = f"""
You are an expert technical recruiter and resume evaluator.

Analyze the candidate's resume against the given job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Evaluate the candidate based ONLY on the information provided.

Return the result as valid JSON with exactly these fields:

{{
    "match_score": 0,
    "strengths": [],
    "skill_gaps": [],
    "reasoning": "",
    "recommendations": []
}}

Rules:

1. match_score must be a number between 0 and 100.
2. strengths must contain important matching skills or experience.
3. skill_gaps must contain skills required by the job but missing or weak in the resume.
4. reasoning should briefly explain why the score was given.
5. recommendations should suggest practical improvements.
6. Do not invent experience that is not present in the resume.
7. Return ONLY valid JSON.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    result_text = response.text.strip()

    # Remove markdown code fences if Gemini returns them
    if result_text.startswith("```"):
        result_text = result_text.replace("```json", "")
        result_text = result_text.replace("```", "")
        result_text = result_text.strip()

    return json.loads(result_text)