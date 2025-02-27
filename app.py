import streamlit as st
import requests
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# OpenRouter API details
API_KEY = os.getenv("API_KEY")  # Load API key from environment variable
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-chat:free"

# Function to call OpenRouter API with retries
def call_openrouter(prompt, max_retries=3, retry_delay=2):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, json=data, headers=headers, timeout=10)
            if response.status_code == 200:
                # Parse and return the response content
                result = response.json()["choices"][0]["message"]["content"]
                return result
            else:
                # Log the error and retry
                print(f"Attempt {attempt + 1} failed: {response.status_code} - {response.text}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)  # Wait before retrying
                else:
                    return f"Error after {max_retries} attempts: {response.status_code} - {response.text}"
        except Exception as e:
            # Handle exceptions like network errors
            print(f"Attempt {attempt + 1} failed with exception: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)  # Wait before retrying
            else:
                return f"Error after {max_retries} attempts: {str(e)}"

# Streamlit App
st.title("Crisis Management Workflow")
st.markdown("[View this project on GitHub](https://github.com/JoelNgiamKeeYong/crisis-management-agent-llm)")
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
    if issue_description.strip() == "":
        st.error("Please enter a crisis scenario.")
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
            
            # Check if the crisis response is valid
            if "Error" in crisis_response:
                st.error("Failed to generate Crisis Management Statement. Please try again.")
            else:
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
                
                # Check if the legal response is valid
                if "Error" in legal_response:
                    st.error("Failed to generate Legal-Safe Press Statement. Please try again.")
                else:
                    # Display Crisis Management Statement
                    st.subheader("🟥 Crisis Management Statement")
                    st.write(crisis_response)
                    
                    # Display Legal-Safe Press Statement
                    st.subheader("🟦 Final Legal-Safe Press Statement")
                    st.write(legal_response)
                    
                    st.success("Legally safe press statement generated!")