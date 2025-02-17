import streamlit as st
import google.generativeai as genai
# Configure Gemini AI with API Key
genai.configure(api_key="AIzaSyAHl04QuirH2-qF98iB45NB8r6Tz-AAHOM")
# System instruction for AI
system_prompt = """You are a Python code reviewer. You should review the code, identify errors,
provide improvements, and give a rating out of 5. Only accept Python code as input."""
# Initialize Gemini AI
gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)
# Streamlit UI
st.title("🚀 Python Code Reviewer with Gemini AI")
st.write("Enter your Python code snippet below, and the AI will review it.")
# Text input for user
user_prompt = st.text_area("🧑‍💻🧑‍💻 Enter your Python code:", height=150)
# Button to process the code
if st.button("🔍🚶‍➡️ Review Code"):
    if user_prompt.strip():
        with st.spinner("Reviewing your code... "):
            response = gemini.generate_content(user_prompt, stream=True)
        # Display AI Review
        st.subheader("✅ AI Review:")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.warning("⚠ Please enter a Python code snippet first.")
