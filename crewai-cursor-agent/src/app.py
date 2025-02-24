import streamlit as st
from crewai import Crew
from tasks.task_factory import TaskFactory
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file if it exists
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Verify API key is available
if not os.getenv('ANTHROPIC_API_KEY'):
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")


def main():
    st.set_page_config(
        page_title="Presentation Creator AI",
        layout="wide",
        theme=os.getenv('STREAMLIT_THEME', 'light')
    )

    st.title("🎯 Throughput Estimation Presentation Creator")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload your PDF article", type=['pdf'])

    if uploaded_file is not None:
        # Create directories if they don't exist
        input_dir = os.getenv('INPUT_DIR', 'input')
        output_dir = os.getenv('OUTPUT_DIR', 'output')
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Save the uploaded file
        pdf_path = os.path.join(input_dir, 'article.pdf')
        with open(pdf_path, 'wb') as f:
            f.write(uploaded_file.getvalue())

        st.success("PDF uploaded successfully!")

        if st.button("Create Presentation"):
            with st.spinner("Creating your presentation..."):
                try:
                    # Create tasks
                    tasks = TaskFactory.create_presentation_tasks(pdf_path)

                    # Create and run the crew
                    crew = Crew(
                        tasks=tasks,
                        verbose=2,
                        process=Crew.Process.sequential
                    )

                    result = crew.kickoff()
                    logger.info("Crew completed tasks successfully")

                    # Check if presentation was created
                    presentation_path = os.path.join(
                        output_dir, "presentation.pptx")
                    if os.path.exists(presentation_path):
                        st.success("Presentation created successfully!")

                        # Provide download button
                        with open(presentation_path, "rb") as file:
                            btn = st.download_button(
                                label="Download Presentation",
                                data=file,
                                file_name="throughput_estimation_presentation.pptx",
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                            )
                    else:
                        st.error("Error: Presentation file not found.")
                        logger.error("Presentation file not created")

                except Exception as e:
                    error_msg = f"An error occurred: {str(e)}"
                    st.error(error_msg)
                    logger.error(error_msg, exc_info=True)
    else:
        st.info("Please upload a PDF article to begin.")


if __name__ == "__main__":
    main()
