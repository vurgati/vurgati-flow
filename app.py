import streamlit as st
from datetime import datetime, timedelta
import json

# Page Configuration
st.set_page_config(
    page_title="Vurgati Flow - AI Business OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Look
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #1E88E5; font-weight: bold;}
    .agent-card {background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1E88E5;}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🚀 Vurgati Flow")
st.sidebar.markdown("**AI Business Operating System**")
st.sidebar.divider()

page = st.sidebar.radio("Navigate", [
    "🏠 Dashboard", 
    "🧠 Flow Brain (Orchestrator)", 
    "📥 Inbox Agent", 
    "✅ Task Agent", 
    "📅 Calendar Agent", 
    "💰 Finance Agent", 
    "📊 Reports"
])

st.sidebar.divider()
st.sidebar.caption("Built live with Vurgati AI OS")

# Shared Memory Simulation
if "memory" not in st.session_state:
    st.session_state.memory = {
        "tasks": [],
        "leads": [],
        "revenue": 2450,
        "today_brief": "Good morning! You have 3 high-priority tasks and 2 new leads."
    }

# ==================== PAGES ====================

if page == "🏠 Dashboard":
    st.title("Welcome to Vurgati Flow")
    st.markdown("### Your Personal + Business AI Operating System")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Tasks", len(st.session_state.memory["tasks"]) or 7, "↑2")
    with col2:
        st.metric("Revenue This Month", f"${st.session_state.memory['revenue']}", "↑12%")
    with col3:
        st.metric("Open Leads", "12", "3 hot")
    with col4:
        st.metric("AI Efficiency", "94%", "↑")
    
    st.divider()
    st.subheader("Today's Morning Brief")
    st.info(st.session_state.memory["today_brief"])
    
    st.subheader("Quick Actions")
    if st.button("🔥 Start Morning Brief"):
        st.success("Flow Brain: Good morning! Here are your top priorities for today.")
    if st.button("📨 Process Inbox"):
        st.success("Inbox Agent: 8 new messages processed → 3 tasks extracted")
    if st.button("📅 Optimize Calendar"):
        st.success("Calendar Agent: Suggested 2 focus blocks + 1 meeting rescheduled")

elif page == "🧠 Flow Brain (Orchestrator)":
    st.title("🧠 Central Orchestrator - Flow Brain")
    st.markdown("**I coordinate all agents and make business decisions.**")
    
    user_input = st.chat_input("Talk to Flow Brain (e.g. 'Schedule client meeting' or 'Process new leads')")
    
    if user_input:
        with st.chat_message("assistant"):
            st.write(f"**Flow Brain:** Understood. Analyzing request: '{user_input}'")
            st.write("→ Assigning to relevant agents...")
            
            if "meeting" in user_input.lower() or "schedule" in user_input.lower():
                st.success("✅ Task Agent + Calendar Agent activated. Proposed times saved.")
                st.session_state.memory["tasks"].append({"task": user_input, "status": "In Progress"})
            elif "lead" in user_input.lower():
                st.success("✅ Sales Agent + Inbox Agent working on it.")
            else:
                st.success("✅ Orchestrator has distributed the task across agents.")

elif page == "📥 Inbox Agent":
    st.title("📥 Inbox Agent")
    st.markdown("**Auto-processes Email, WhatsApp, and Messages**")
    
    st.text_area("Paste message or forward simulation", "Client said they want to move forward with the project...")
    if st.button("Process Message"):
        st.success("Message processed! Task created + Follow-up scheduled + Note saved to Knowledge Base")

elif page == "✅ Task Agent":
    st.title("✅ Task & Project Agent")
    st.subheader("Active Tasks")
    
    new_task = st.text_input("Add new task")
    if st.button("Add Task") and new_task:
        st.session_state.memory["tasks"].append({"task": new_task, "status": "New"})
        st.success("Task added and prioritized!")
    
    for i, task in enumerate(st.session_state.memory["tasks"]):
        st.checkbox(task["task"], key=i)

elif page == "📅 Calendar Agent":
    st.title("📅 Calendar Agent")
    st.write("Smart Scheduling & Time Protection")
    
    col1, col2 = st.columns(2)
    with col1:
        st.date_input("Select date", datetime.now().date())
    with col2:
        st.time_input("Preferred time")
    
    if st.button("Find Best Slot"):
        st.success("✅ Best slot found: Tomorrow 11:00 AM (2-hour focus block protected)")

elif page == "💰 Finance Agent":
    st.title("💰 Finance Intelligence Agent")
    st.metric("Projected Revenue", "$8,450", "↑18%")
    st.metric("Outstanding Invoices", "$1,200", "2 invoices")
    
    if st.button("Chase Payments"):
        st.success("Payment reminders sent automatically to 2 clients")

elif page == "📊 Reports":
    st.title("Weekly Performance Report")
    st.success("System running at 94% autonomy")
    st.bar_chart({"Mon": 4, "Tue": 7, "Wed": 5, "Thu": 8, "Fri": 6})

# Footer
st.caption("Vurgati Flow MVP • Powered by VURGATI AI OS • Zero Cost Prototype")
