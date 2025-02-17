import streamlit as st
import google.generativeai as genai
import os

# Secure API Key handling
genai.configure(api_key=os.getenv("AIzaSyAHl04QuirH2-qF98iB45NB8r6Tz-AAHOM"))  # Use environment variable or Streamlit secrets

# System instruction as context
sys_prompt = """
You are an AI code reviewer. You will analyze Python code for potential bugs, errors,
and areas of improvement. Provide detailed feedback and suggest fixes.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Use a valid model name

def review_code(user_code):
    """Send user code to the AI model for review and return the response."""
    try:
        response = model.generate_content([sys_prompt, user_code])  # Pass sys_prompt in request
        return response.candidates[0].text if response.candidates else "No response received from AI."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI Code Reviewer")
st.write("Submit your Python code for review and receive feedback!")

user_code = st.text_area("Enter your Python code here:")

if st.button("Review Code"):
    if user_code.strip():
        feedback = review_code(user_code)
        st.subheader("Review Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")
