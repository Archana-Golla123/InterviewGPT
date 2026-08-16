import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def evaluate_answer(question, answer):

    prompt = f"""
You are an AI interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Provide:

1. Score out of 10
2. Strengths
3. Weaknesses
4. Suggestions for improvement
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content