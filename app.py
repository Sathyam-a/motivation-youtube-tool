import streamlit as st
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY environment variable set nahi hai")
    st.stop()

client = OpenAI(api_key=api_key)
