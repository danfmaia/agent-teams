import streamlit as st

# Configure page
st.set_page_config(
    page_title="Presentation Generator",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("Workflow Progress")
st.sidebar.markdown("---")

# Main content
st.title("📊 Automated Presentation Generator")
st.markdown("Generating a 5-minute presentation about Throughput Estimation")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'current_step' not in st.session_state:
    st.session_state.current_step = "Initializing"
