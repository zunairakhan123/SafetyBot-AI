

import streamlit as st

# Access the secrets from Streamlit's `secrets` storage
GROQ_API_KEY = st.secrets["GROQ"]["GROQ_API_KEY"]
MODEL_NAME = st.secrets["GROQ"]["MODEL_NAME"]
SAFE_PROMPT_PREFIX = st.secrets["GROQ"]["SAFE_PROMPT_PREFIX"]