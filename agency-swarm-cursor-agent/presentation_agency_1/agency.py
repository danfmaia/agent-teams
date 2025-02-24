import os
from dotenv import load_dotenv
from agency_swarm.agency import Agency
from research_agent.research_agent import ResearchAgent
from presentation_agent.presentation_agent import PresentationAgent
from research_agent.tools.PDFReader import PDFReader
from presentation_agent.tools.PPTXCreator import PPTXCreator

# Load environment variables
load_dotenv()


def main():
    try:
        # Check if OpenAI API key is set
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "OPENAI_API_KEY not found in environment variables")

        # Initialize agents
        research_agent = ResearchAgent()
        presentation_agent = PresentationAgent()

        # Create the agency with communication flows
        agency = Agency(
            [
                research_agent,  # Research Agent will be the entry point
                # Research Agent can communicate with Presentation Agent
                [research_agent, presentation_agent],
            ],
            shared_instructions="agency_manifesto.md",
            temperature=0.7,
            max_prompt_tokens=25000
        )

        print("Agency initialized successfully!")

        # Process the PDF and create presentation
        process_document(research_agent, presentation_agent)

        return agency

    except Exception as e:
        print(f"Error initializing agency: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def process_document(research_agent, presentation_agent):
    """Process the document and create the presentation"""
    try:
        print("\nStep 1: Reading and analyzing PDF...")
        # Read and analyze the PDF
        pdf_reader = PDFReader(pdf_path="input/06170058.pdf")
        pdf_result = pdf_reader.run()

        if not isinstance(pdf_result, dict):
            print("Error reading PDF:", pdf_result)
            return

        print(f"\nSuccessfully read PDF with {pdf_result['num_pages']} pages")
        print("\nSections found:")
        for section, content in pdf_result['sections'].items():
            if content:
                print(f"- {section.title()}: {len(content)} characters")
            else:
                print(f"- {section.title()}: Not found")

        print("\nStep 2: Creating presentation...")
        # Create the presentation
        pptx_creator = PPTXCreator(
            content=pdf_result,
            output_path="output/throughput_presentation.pptx"
        )
        pptx_result = pptx_creator.run()
        print(pptx_result)

    except Exception as e:
        print(f"Error processing document: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    agency = main()
    if agency:
        print("\nStarting agency demo...")
        agency.run_demo()
