import streamlit as st
from datetime import datetime
import time
import random

st.set_page_config(page_title="V-Business", page_icon="🦁", layout="wide")

# Apple × Tesla × Jarvis Premium Dark UI
st.markdown("""
<style>
    .main {background-color: #050505; color: #E0E0E0;}
    .stApp {background-color: #050505;}
    .main-header {font-size: 3.4rem; font-weight: 800; background: linear-gradient(90deg, #FFFFFF, #00E5FF, #FFFFFF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .agent-card {background: rgba(0,229,255,0.05); border: 1px solid rgba(0,229,255,0.3); border-radius: 16px; padding: 20px; margin: 10px 0;}
    .log {background: #111111; padding: 14px; border-radius: 10px; border-left: 4px solid #00E5FF; margin: 6px 0;}
</style>
""", unsafe_allow_html=True)

# Header with Logo
col1, col2 = st.columns([1,6])
with col1:
    st.image("https://i.imgur.com/8vN9kL2.png", width=110)  # Replace with your real logo URL
with col2:
    st.markdown('<h1 class="main-header">V-BUSINESS</h1>', unsafe_allow_html=True)
    st.caption("🦁 Autonomous AI Operating System • AI Departments Running 24/7")

st.sidebar.image("https://i.imgur.com/8vN9kL2.png", width=130)
st.sidebar.title("V-BUSINESS OS")
st.sidebar.markdown("**Executive Command**")

page = st.sidebar.radio("SYSTEM", [
    "🏠 Executive Command Center",
    "🧠 Central Orchestrator",
    "📈 Sales Department",
    "🚀 Marketing Department",
    "🛟 Support Department",
    "⚙️ Operations Department",
    "💰 Finance Department",
    "📊 Live Company Pulse"
])

# Shared Business Memory
if "company" not in st.session_state:
    st.session_state.company = {
        "revenue": 34780,
        "leads": 68,
        "customers": 156,
        "autonomy": 91,
        "activity": ["Orchestrator online", "Marketing launched campaign", "Finance updated forecast"]
    }

if page == "🏠 Executive Command Center":
    st.title("🏠 Executive Command Center")
    
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric("Revenue", f"${st.session_state.company['revenue']:,}", "↑26%")
    with c2: st.metric("Pipeline Leads", st.session_state.company['leads'], "↑11")
    with c3: st.metric("Active Customers", st.session_state.company['customers'])
    with c4: st.metric("AI Autonomy", f"{st.session_state.company['autonomy']}%", "↑4%")
    
    st.divider()
    st.subheader("🌅 Executive Brief")
    st.info("**Central Orchestrator:** Revenue on track. Sales closing rate improved 14%. Marketing ROI at 4.8x. 3 departments recommend budget reallocation.")
    
    goal = st.text_input("Set High-Level Goal (e.g. 'Increase revenue by 20% this quarter')")
    if st.button("🚀 Deploy Goal to All Departments", type="primary", use_container_width=True):
        with st.spinner("Orchestrator planning and delegating..."):
            time.sleep(2)
            st.success("✅ Goal deployed. All departments activated and coordinating.")
            st.session_state.company["activity"].append(f"Goal executed: {goal[:60]}...")

elif page == "🧠 Central Orchestrator":
    st.title("🧠 Central Orchestrator")
    st.markdown("**The Brain — Coordinates all departments like a real COO**")
    
    if "chat" not in st.session_state: st.session_state.chat = []
    
    for m in st.session_state.chat:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    
    cmd = st.chat_input("Speak to the Company (e.g. Increase revenue by 20%, Prepare Q3 strategy)")
    if cmd:
        st.session_state.chat.append({"role": "user", "content": cmd})
        with st.chat_message("assistant"):
            resp = f"**Orchestrator Activated**\n\nCommand: {cmd}\n\n"
            resp += "• Sales: Lead qualification ramped up\n"
            resp += "• Marketing: New campaign assets generated\n"
            resp += "• Finance: Impact modeled (+$9.2k projected)\n"
            resp += "• Operations: Workflows updated"
            st.write(resp)
            st.session_state.chat.append({"role": "assistant", "content": resp})
            st.session_state.company["activity"].append(f"Orchestrator: {cmd[:50]}")

elif page == "📈 Sales Department":
    st.title("📈 Sales Department")
    if st.button("Run Full Sales Cycle"):
        st.success("✅ 18 leads qualified • 5 proposals sent • 2 deals closed ($4,800) • Pipeline updated")

elif page == "🚀 Marketing Department":
    st.title("🚀 Marketing Department")
    if st.button("Launch Autonomous Campaign"):
        st.success("✅ Content created for 6 channels • Ads optimized • 27 new leads projected")

elif page == "🛟 Support Department":
    st.title("🛟 Support Department")
    if st.button("Process All Tickets"):
        st.success("✅ 14 tickets resolved • 2 upsells identified • CSAT: 4.95/5")

elif page == "⚙️ Operations Department":
    st.title("⚙️ Operations Department")
    if st.button("Optimize All Workflows"):
        st.success("✅ SOPs updated • Automations synchronized • Bottlenecks cleared")

elif page == "💰 Finance Department":
    st.title("💰 Finance Department")
    st.metric("Cash Position", f"${st.session_state.company['revenue']:,}")
    if st.button("Run Financial Intelligence"):
        st.success("✅ Forecast updated • 4 invoices chased • Profit optimization suggestions ready")

elif page == "📊 Live Company Pulse":
    st.title("📊 Live Company Pulse")
    for act in reversed(st.session_state.company["activity"][-12:]):
        st.markdown(f"<div class='log'>🟢 {act}</div>", unsafe_allow_html=True)
    st.success("All departments online and collaborating in real time.")

st.caption("V-Business • Autonomous AI Company OS • Vision: Full AI Workforce Infrastructure • Built live by VURGATI AI OS")
