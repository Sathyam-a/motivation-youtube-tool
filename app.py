import streamlit as st
import os
from openai import OpenAI

# ================== OPENAI SETUP ==================
# Make sure your API key is saved in Streamlit Secrets as OPENAI_API_KEY
# OR locally as environment variable
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OpenAI API Key missing! Add it in Streamlit Secrets or as environment variable OPENAI_API_KEY.")
    st.stop()

client = OpenAI(api_key=api_key)

# ================== UI ==================
st.set_page_config(page_title="Motivation YouTube Growth Assistant", layout="centered")
st.title("🔥 Motivation YouTube Growth Assistant")
st.caption("🚀 Complete AI YouTube Automation Tool")

topic = st.text_input("Enter Topic (e.g. success, failure, discipline, money, study)")

language = st.selectbox(
    "Choose Script Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Long Video", "YouTube Short / Reel"]
)

# ================== BUTTON ==================
if st.button("🚀 Generate Full YouTube Growth Kit"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("AI is creating viral content... 🔥"):
            prompt = f"""
            You are a professional YouTube growth expert.

            Create COMPLETE YouTube content for:
            Topic: {topic}
            Language: {language}
            Content Type: {content_type}

            Give output in this format:

            1. 10 Viral Video Titles
            2. 10 SEO Hashtags
            3. Strong 3-line Hook (first 5 seconds)
            4. Full Emotional Motivational Script
            5. CTA (Like, Subscribe, Comment)
            6. 3 Short/Reel Ideas

            Make it emotional, powerful and viral.
            """

            try:
                response = client.responses.create(
                    model="gpt-4o-mini",  # safe model
                    input=prompt
                )

                output = response.output_text

                st.success("✅ Content Generated Successfully!")
                st.subheader("📌 Your AI Generated Content")
                st.text_area("Output", output, height=500)

            except Exception as e:
                st.error(f"❌ Error generating content: {e}")
