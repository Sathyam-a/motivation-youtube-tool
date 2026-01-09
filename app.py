import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Motivation YouTube Growth Assistant",
    page_icon="🔥",
    layout="centered"
)

# ================= HEADER =================
st.title("🔥 Motivation YouTube Growth Assistant")
st.caption("🚀 YouTube Content Helper (No AI • Fully Stable)")

st.divider()

# ================= INPUTS =================
topic = st.text_input("Enter Topic (e.g. success, discipline, money, study)")

language = st.selectbox(
    "Choose Language",
    ["English", "Hindi", "Hinglish"]
)

content_type = st.selectbox(
    "Choose Content Type",
    ["YouTube Short / Reel", "Long Video"]
)

niche = st.selectbox(
    "Choose Niche",
    ["Motivation", "Study", "Money", "Gym / Fitness"]
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
            f"Nobody Talks About {topic}",
            f"If You Feel Lost, Listen This About {topic}",
            f"How {topic} Can Change Your Life"
        ]
        st.write("\n".join([f"• {t}" for t in titles]))

        # ================= HOOK =================
        st.subheader("🎯 Killer Hook (First 3 Seconds)")
        st.write(f"No one warns you about this side of {topic}…")

        # ================= SCRIPT =================
        st.subheader("📝 Emotional Script")

        if language == "Hindi":
            script = f"""
Sab {topic} chahte hain,
lekin sacrifice koi nahi karta.

Jo aaj pain se bhaag raha hai,
kal wahi regret karega.
"""
        elif language == "Hinglish":
            script = f"""
Sabko {topic} chahiye,
par struggle koi nahi chahta.

Agar tu abhi bhi laga hua hai,
tu already 90% logon se aage hai.
"""
        else:
            script = f"""
Everyone wants {topic},
but nobody wants the struggle.

This phase decides
who quits and who wins.
"""

        st.text_area("Copy Script 👇", script, height=180)

        # ================= HASHTAGS =================
        st.subheader("🔖 SEO Hashtags")
        hashtags = f"""
#{topic.replace(" ", "")}
#{niche.replace(" ", "")}
#motivation
#success
#mindset
"""
        st.code(hashtags)

        # ================= CTA =================
        st.subheader("📣 Call To Action (CTA)")
        st.write("👍 Like | 🔔 Subscribe | 💬 Comment")

        # ================= SHORT IDEAS =================
        st.subheader("🎬 Short / Reel Ideas")
        shorts = [
            f"1 powerful line about {topic}",
            f"Pain of being average in {topic}",
            f"Why most people fail at {topic}"
        ]
        for s in shorts:
            st.write("•", s)
