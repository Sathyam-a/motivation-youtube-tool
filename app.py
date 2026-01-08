import streamlit as st

st.title("🔥 Motivation YouTube Growth Assistant")

st.subheader("🎯 Video Idea Generator")

topic = st.text_input("Enter topic (e.g. success, failure, discipline)")

if st.button("Generate Ideas"):
    if topic:
        st.write("✅ Video Ideas:")
        st.write(f"1. How {topic} can change your life")
        st.write(f"2. The dark truth about {topic}")
        st.write(f"3. Nobody talks about {topic}")
        st.write(f"4. 5 lessons about {topic} that will make you unstoppable")
        st.write(f"5. If you feel lost, listen to this about {topic}")
    else:
        st.warning("Please enter a topic")
