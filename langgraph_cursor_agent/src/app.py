import asyncio
from pathlib import Path

import streamlit as st

from workflow import create_workflow, create_initial_state


# Constants
PPTX_MIME_TYPE = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

# Configure page
st.set_page_config(
    page_title="Presentation Generator",
    page_icon="📊",
    layout="wide"
)

# Initialize workflow
workflow = create_workflow()
initial_state = create_initial_state()

# Sidebar - Workflow Progress
st.sidebar.title("🔄 Workflow Progress")
st.sidebar.markdown("---")

# Initialize session state for progress tracking
if 'agent_status' not in st.session_state:
    st.session_state.agent_status = {
        'pdf_reader': '⏳ Waiting',
        'translator': '⏳ Waiting',
        'designer': '⏳ Waiting',
        'reviewer': '⏳ Waiting',
        'improver': '⏳ Waiting'
    }

# Display agent status in sidebar
for agent, status in st.session_state.agent_status.items():
    st.sidebar.text(f"{status} {agent.replace('_', ' ').title()}")

# Main content
st.title("📊 Automated Presentation Generator")
st.markdown("""
Generate a 5-minute presentation in Portuguese from a technical article.

1. Upload a PDF article about Throughput Estimation
2. Click 'Generate Presentation'
3. Monitor the progress in the sidebar
4. Download the final presentation
""")

# File uploader
uploaded_file = st.file_uploader("Upload PDF article", type="pdf")

if uploaded_file:
    # Create input directory if it doesn't exist
    input_dir = Path("input")
    input_dir.mkdir(exist_ok=True)

    # Save uploaded file
    pdf_path = input_dir / "article.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    st.success("✅ PDF uploaded successfully!")

    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    if st.button("🚀 Generate Presentation"):
        progress_bar = st.progress(0)
        status_text = st.empty()

        with st.spinner("Generating presentation..."):
            try:
                # Run workflow
                def update_progress(state):
                    """Update progress based on current agent"""
                    agent_order = ['pdf_reader', 'translator',
                                   'designer', 'reviewer', 'improver']
                    current = state.get('current_agent', '').lower().replace(
                        ' agent', '').replace(' ', '_')

                    # Update status
                    for agent in st.session_state.agent_status:
                        if agent == current:
                            st.session_state.agent_status[agent] = '🔄 Running'
                        elif agent_order.index(agent) < agent_order.index(current):
                            st.session_state.agent_status[agent] = '✅ Done'

                    # Update progress bar
                    if current in agent_order:
                        progress = (agent_order.index(
                            current) + 1) / len(agent_order)
                        progress_bar.progress(progress)
                        status_text.text(
                            f"Current step: {current.replace('_', ' ').title()}")

                    return state

                # Add progress callback to workflow
                workflow.set_state_callback(update_progress)

                final_state = asyncio.run(workflow.invoke(initial_state))

                # Check for errors
                if final_state["errors"]:
                    st.error("❌ Errors occurred during generation:")
                    for error in final_state["errors"]:
                        st.error(error)
                else:
                    st.success("✅ Presentation generated successfully!")
                    progress_bar.progress(1.0)
                    status_text.text("Complete!")

                    # Show presentation stats
                    if "presentation" in final_state:
                        st.markdown("### 📊 Presentation Statistics")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Number of Slides",
                                      len(final_state["presentation"]["slides"]))
                        with col2:
                            st.metric("Estimated Duration",
                                      f"{final_state['presentation']['total_time']:.1f} min")
                        with col3:
                            st.metric("Version",
                                      final_state["presentation"]["current_version"])

                    # Download button
                    with open("output/presentation.pptx", "rb") as f:
                        pptx_data = f.read()
                        st.download_button(
                            label="⬇️ Download Presentation",
                            data=pptx_data,
                            file_name="presentation.pptx",
                            mime=PPTX_MIME_TYPE
                        )

            except Exception as e:
                st.error(f"❌ Error generating presentation: {str(e)}")
                # Reset progress
                progress_bar.progress(0)
                status_text.text("Error occurred")

# Display messages
if "messages" in st.session_state:
    st.markdown("### 📝 Process Log")
    for msg in st.session_state.messages:
        st.text(msg)
