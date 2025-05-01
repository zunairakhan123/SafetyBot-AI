import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
MODEL_NAME = "llama3-8b-8192"
SAFE_PROMPT_PREFIX = "You are a friendly and safe AI mentor for kids and teens. Respond positively and constructively."
