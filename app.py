import streamlit as st
from openai import OpenAI

# OpenAI client (API key environment variable se lega)
client = OpenAI()

st.set_page_config(page_title="YouTube Tool", page_icon="🎥")
st.title("🎥 YouTube Video Content Generator")

st.write("Apne YouTube video ke liye Title, Description aur Hashtags generate karo 🚀")

# User inputs
topic = st.text_input("📌 Video Topic (kis topic par video hai?)")
language = st.selectbox("🌐 Language", ["Hindi", "English"])
tone = st.selectbox("🔥 Tone", ["Motivational", "Emotional", "Informative", "Funny"])

if st.button("✨ Generate"):
    if topic == "":
        st.warning("Pehle video topic likho")
    else:
        prompt = f"""
        Generate YouTube content for the following video.

        Topic: {topic}
        Language: {language}
        Tone: {tone}

        Give output in this format:

        Title:
        Description:
        Hashtags:
        """

        with st.spinner("Generating content..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        result = response.choices[0].message.content

        st.success("✅ Content Generated")

        st.markdown("### 🏷️ Title")
        st.write(result.split("Description:")[0].replace("Title:", "").strip())

        st.markdown("### 📝 Description")
        st.write(
            result.split("Description:")[1]
            .split("Hashtags:")[0]
            .strip()
        )

        st.markdown("### 🔖 Hashtags")
        st.write(
            result.split("Hashtags:")[1].strip()
        )
