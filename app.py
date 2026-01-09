import streamlit as st

st.set_page_config(
    page_title="Motivation YouTube Growth Assistant",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 Motivation YouTube Growth Assistant")
st.subheader("🚀 YouTube Content Helper (No AI – Stable Version)")

st.divider()

topic = st.text_input("Enter Topic (e.g. success, discipline, money, study)")

language = st.selectbox(
    "Choose Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Short", "Reel", "Long Video"]
)

if st.button("Generate Content"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        st.success("✅ Content Generated")

        st.markdown("### 📌 Video Title")
        st.write(f"The Dark Truth About {topic}")

        st.markdown("### 🔖 Hashtags")
        st.write(f"#{topic} #motivation #success #mindset #life")

        st.markdown("### 🎯 Hook (First 3 seconds)")
        st.write(f"No one talks about this truth of {topic}...")

        st.markdown("### 📝 Short Script")
        if language == "Hindi":
            st.write(f"{topic} sab chahte hain, par sacrifice koi nahi karta.")
        elif language == "Hinglish":
            st.write(f"Sabko {topic} chahiye, par pain koi nahi chahta.")
        else:
            st.write(f"Everyone wants {topic}, but no one wants the pain.")
