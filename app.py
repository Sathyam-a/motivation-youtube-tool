import streamlit as st

st.set_page_config(page_title="Motivation YouTube Growth Assistant", page_icon="🔥")

st.title("🔥 Motivation YouTube Growth Assistant")
st.subheader("🎯 Video Idea + Script Generator")

topic = st.text_input("Enter topic (e.g. success, failure, discipline)")

content_type = st.selectbox(
    "Choose content type",
    ["YouTube Short (30 sec)", "YouTube Reel", "Long Video Intro"]
)

if st.button("Generate Content"):
    if topic:
        st.success("Content Generated Successfully 🚀")

        st.markdown("### ✅ Video Idea")
        st.write(f"*The dark truth about {topic}*")

        st.markdown("### 📝 Ready-to-Use Script")

        if content_type == "YouTube Short (30 sec)":
            script = f"""
Success in {topic} is not easy.
People see the results,
but they don’t see the sacrifices.
If you feel tired,
remember — this phase is building you.
Don’t quit. Keep going.
"""
        elif content_type == "YouTube Reel":
            script = f"""
Everyone wants {topic},
but no one wants the struggle.
Pain is temporary.
Discipline creates freedom.
Stay focused.
"""
        else:
            script = f"""
Today we talk about {topic}.
Not the fake motivation,
but the real truth.
If you want growth,
you must embrace discomfort.
Let’s begin.
"""

        st.text_area("Copy Script 👇", script, height=200)

    else:
        st.warning("Please enter a topic first!")
