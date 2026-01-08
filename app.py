import streamlit as st

st.set_page_config(
    page_title="Motivation YouTube Growth Assistant",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 Motivation YouTube Growth Assistant")
st.subheader("🚀 Complete AI YouTube Automation Tool")

st.divider()

topic = st.text_input("Enter topic (e.g. success, discipline)")

language = st.selectbox(
    "Choose Script Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Short", "Reel", "Long Video"]
)

if st.button("Generate Full YouTube Growth Kit"):
    st.success("Working ✅")
