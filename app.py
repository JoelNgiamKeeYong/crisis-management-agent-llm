import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenRouter API details
API_KEY = st.secrets["SECRET_KEY"]
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-chat:free"

# Function to call OpenRouter API
def call_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_URL, json=data, headers=headers, timeout=10)  # 10-second timeout
        if response.status_code == 200:
            response_json = response.json()
            if "choices" in response_json and len(response_json["choices"]) > 0:
                return response_json["choices"][0]["message"]["content"]
            else:
                st.error("Invalid API response format.")
                return None
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.Timeout:
        st.error("The API request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
        return None

# Streamlit App
st.title("Crisis Management Workflow")
st.markdown("""
This app leverages a sophisticated multi-agent workflow powered by LangChain to generate two essential press statements for any crisis scenario:

1. **Crisis Management Statement**: Drafted by a crisis management expert, this statement acknowledges the issue, reassures stakeholders, and outlines the steps being taken to resolve the crisis.
   
2. **Legally Safe Press Statement**: Reviewed by a legal expert, this statement refines the initial response to ensure it avoids any direct admission of fault or legal liability while maintaining a professional and reassuring tone.

Both statements are tailored to handle crisis situations while protecting the company’s reputation and legal standing.
""")

# Input: Crisis Description
issue_description = st.text_area(
    "Describe the crisis scenario:",
    placeholder="E.g., Kia recalls 80,000 vehicles due to faulty wiring, improper air bag deployment"
)

# Button to run the workflow
if st.button("Generate Statements"):
    if not issue_description.strip():
        st.error("Please enter a valid crisis scenario.")
    else:
        with st.spinner("Generating responses..."):
            # Generate Crisis Management Statement
            crisis_prompt = f"""
            You are a crisis management expert.
            Draft a **short and professional statement for the press** addressing the crisis while maintaining trust in the company.
            Your response should:
            - Acknowledge the issue.
            - Reassure customers, stakeholders, and the public.
            - Briefly mention the steps being taken to resolve the situation.
            - Be concise, clear, and confident.

            Crisis Situation: {issue_description}

            Press Statement:
            """
            crisis_response = call_openrouter(crisis_prompt)

            if crisis_response:
                # Generate Legal-Safe Press Statement
                legal_prompt = f"""
                You are a legal expert.
                Review the following short press statement and edit it to (1) deny the direct culpability, and (2) remove any language that could put the company in legal liability.
                Ensure the statement remains professional and reassuring but avoids making admissions of fault or liability.
                In the final shared statement, please add a note about what your changed from the original statement and why, giving at least 1 concrete example.

                Crisis Situation: {issue_description}

                Original Press Statement:
                {crisis_response}

                Legally Safe Press Statement:
                """
                legal_response = call_openrouter(legal_prompt)

                if legal_response:
                    # Display Crisis Management Statement
                    st.subheader("🟥 Crisis Management Statement")
                    st.write(crisis_response)

                    # Display Legal-Safe Press Statement
                    st.subheader("🟦 Final Legal-Safe Press Statement")
                    st.write(legal_response)

                    # Final
                    st.success("Statements saved to 'crisis_response_output.json'.")