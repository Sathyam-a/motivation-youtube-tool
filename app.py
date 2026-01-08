import streamlit as st

st.set_page_config(page_title="Motivation YouTube Growth Assistant", page_icon="🔥")

st.title("🔥 Motivation YouTube Growth Assistant")
st.subheader("🚀 All-in-One YouTube Growth Tool")

topic = st.text_input("Enter topic (e.g. success, failure, discipline)")

content_type = st.selectbox(
    "Choose content type",
    ["YouTube Short", "Reel", "Long Video"]
)

if st.button("Generate Full Content"):
    if topic:
        st.success("🔥 Content Generated Successfully!")

        # 🔹 HOOK
        st.markdown("## 🎯 Killer Hook (First 3 Seconds)")
        hook = f"Nobody talks about this truth of {topic}..."
        st.write(hook)

        # 🔹 VIDEO IDEA
        st.markdown("## 💡 Video Idea")
        st.write(f"The dark truth about {topic} that will change your mindset")

        # 🔹 SCRIPT
        st.markdown("## 📝 Ready-to-Use Script")
        script = f"""
People want {topic},
but they don’t want the pain.
Late nights. Self-doubt.
No motivation.
But this phase?
This is what builds legends.
Don’t quit now.
"""
        st.text_area("Copy Script 👇", script, height=200)

        # 🔹 TITLE
        st.markdown("## 🧠 SEO Optimized Title")
        title = f"The Dark Truth About {topic} | Motivation 🔥"
        st.write(title)

        # 🔹 DESCRIPTION
        st.markdown("## 📄 Video Description")
        description = f"""
This video reveals the dark truth about {topic}.
If you are feeling lost, tired, or confused —
this message is for you.

Watch till the end and stay focused.
"""
        st.text_area("Copy Description 👇", description, height=150)

        # 🔹 HASHTAGS
        st.markdown("## 🏷️ Viral Hashtags")
        hashtags = f"""
#{topic.replace(" ", "")}
#Motivation
#SuccessMindset
#SelfDiscipline
#LifeMotivation
#DailyMotivation
"""
        st.code(hashtags)

    else:
        st.warning("⚠️ Please enter a topic first!")
