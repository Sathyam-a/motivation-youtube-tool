import streamlit as st

st.set_page_config(page_title="Motivation YouTube Growth Assistant", page_icon="🔥")

st.title("🔥 Motivation YouTube Growth Assistant")
st.subheader("🚀 Complete AI YouTube Automation Tool")

# ---------------- INPUTS ----------------
topic = st.text_input("Enter topic (or leave empty for trending ideas)")

language = st.selectbox(
    "Choose Script Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Short", "Reel", "Long Video"]
)

# ---------------- BUTTON ----------------
if st.button("Generate Full YouTube Growth Kit"):

    # 🔹 TRENDING TOPICS
    if not topic:
        st.markdown("## 🔥 Trending Motivation Topics")
        trending = [
            "Discipline beats motivation",
            "Pain of being average",
            "Hard work vs luck",
            "Why most people fail",
            "Late night grind"
        ]
        for t in trending:
            st.write("•", t)
        st.stop()

    st.success("🚀 Your Content Is Ready!")

    # ---------------- HOOK ----------------
    st.markdown("## 🎯 Killer Hook (First 3 Seconds)")
    st.write(f"No one talks about this truth of {topic}...")

    # ---------------- SCRIPT ----------------
    st.markdown("## 📝 Emotional Script")

    if language == "Hindi":
        script = f"""
Sab {topic} chahte hain,
lekin struggle nahi.
Jab pain aata hai,
log ruk jaate hain.

Yaad rakhna —
jo rukta hai, wahi haar ta hai.
"""
    elif language == "Hinglish":
        script = f"""
Sabko {topic} chahiye,
par sacrifice koi nahi karta.
Pain aaye toh log give up kar dete hain.

Agar tu abhi bhi khada hai,
tu already alag hai.
"""
    else:
        script = f"""
Everyone wants {topic},
but no one wants the pain.
Late nights. Doubt. Silence.

But this phase?
This is where winners are born.
"""

    st.text_area("Copy Script 👇", script, height=200)

    # ---------------- TITLE ----------------
    st.markdown("## 🧠 SEO Optimized Title")
    title = f"The Dark Truth About {topic} | Motivation 🔥"
    st.write(title)

    # ---------------- DESCRIPTION ----------------
    st.markdown("## 📄 Video Description")
    description = f"""
This video explains the real truth about {topic}.
If you feel lost, tired or unmotivated,
this message is for you.
