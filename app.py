import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Motivation YouTube Growth Assistant",
    page_icon="🔥",
    layout="centered"
)

# ================= HEADER =================
st.title("🔥 Motivation YouTube Growth Assistant")
st.caption("🚀 Complete YouTube Content Generator (No AI, Fully Stable)")

st.divider()

# ================= INPUTS =================
topic = st.text_input("Enter Topic (e.g. success, discipline, failure, money)")

language = st.selectbox(
    "Choose Script Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Short / Reel", "Long Video"]
)

# ================= BUTTON =================
if st.button("🚀 Generate YouTube Growth Kit"):

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic first")
    else:
        st.success("✅ Content Generated Successfully!")

        # ================= TITLES =================
        st.subheader("📌 Viral Video Titles")
        titles = [
            f"The Dark Truth About {topic}",
            f"Why {topic} Is So Hard",
            f"If You Feel Lost, Listen This About {topic}",
            f"Nobody Talks About {topic}",
            f"How {topic} Can Change Your Life"
        ]
        for t in titles:
            st.write("•", t)

        # ================= HOOK =================
        st.subheader("🎯 Killer Hook (First 3 Seconds)")
        st.write(f"No one warns you about this side of {topic}…")

        # ================= SCRIPT =================
        st.subheader("📝 Emotional Script")

        if language == "Hindi":
            script = f"""
Sab {topic} chahte hain,
lekin struggle koi nahi.

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
but nobody wants the pain.

Late nights. Doubt. Silence.
This phase decides who wins.
"""

        st.text_area("Copy Script 👇", script, height=200)

        # ================= HASHTAGS =================
        st.subheader("🔖 SEO Hashtags")
        hashtags = [
            f"#{topic.replace(' ', '')}",
            "#motivation",
            "#success",
            "#mindset",
            "#selfimprovement"
        ]
        st.write(" ".join(hashtags))

        # ================= CTA =================
        st.subheader("📣 Call To Action (CTA)")
        st.write("Like 👍 | Subscribe 🔔 | Comment 💬")

        # ================= SHORT IDEAS =================
        st.subheader("🎬 Short / Reel Ideas")
        shorts = [
            f"1 line truth about {topic}",
            f"Pain of {topic} (relatable clip)",
            f"Why most people fail at {topic}"
        ]
        for s in shorts:
            st.write("•", s)
