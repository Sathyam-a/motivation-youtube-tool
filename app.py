import streamlit as st
from openai import OpenAI

# ================== OPENAI SETUP ==================
client = OpenAI(
    api_key="PASTE_YOUR_OPENAI_API_KEY_HERE"
)

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

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            output = response.output_text

        st.success("✅ Content Generated Successfully!")

        st.subheader("📌 Your AI Generated Content")
        st.text_area("Output", output, height=500)
