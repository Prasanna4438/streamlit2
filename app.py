import streamlit as st
import google.generativeai as genai
import os

# Secure API Key Handling
api_key = os.getenv("GEMINI_API_KEY")  # Store API key in environment variable
if not api_key:
    st.error("API key is missing! Set GEMINI_API_KEY as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

sys_prompt = """
You are an AI code reviewer. You will analyze Python code for potential bugs, errors,
and areas of improvement. Provide detailed feedback and suggest fixes.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-flash", 
                              system_instruction=sys_prompt)

def review_code(user_code):
    """Send user code to the AI model for review and return the response."""
    try:
        response = model.generate_content(user_code)
        return response.text if response else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🤖 AI Code Reviewer")
st.write("Submit your Python code for review and receive feedback!")

user_code = st.text_area("Enter your Python code here:")

if st.button("🔍 Review Code"):
    if user_code.strip():
        feedback = review_code(user_code)
        st.subheader("📌 Review Feedback:")
        st.markdown(feedback)
    else:
        st.warning("⚠️ Please enter some Python code before submitting.")
