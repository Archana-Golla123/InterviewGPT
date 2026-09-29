import streamlit as st
from groq import Groq


def evaluate_answer(question, answer):

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert interview evaluator."
            },
            {
                "role": "user",
                "content": f"""
Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer and provide:

1. Score out of 10
2. Strengths
3. Weaknesses
4. Improvement suggestions
5. Better sample answer
"""
            }
        ],
        temperature=0.3,
        max_tokens=1000
    )

    return response.choices[0].message.content