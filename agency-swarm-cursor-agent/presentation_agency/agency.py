import os
from agency_swarm import Agency
from ResearchAgent import ResearchAgent
from ContentWriter import ContentWriter
from PresentationDesigner import PresentationDesigner
from QAAgent import QAAgent
from results_manager import ResultsManager


class PresentationAgency(Agency):
    def __init__(self):
        # Initialize results manager
        self.results_manager = ResultsManager()

        # Initialize agents
        research = ResearchAgent()
        writer = ContentWriter()
        designer = PresentationDesigner()
        qa = QAAgent()

        # Define communication flows
        super().__init__(
            [
                research,  # Research agent is the entry point
                [research, writer],  # Research can communicate with Writer
                [writer, designer],  # Writer can communicate with Designer
                [designer, qa],  # Designer can communicate with QA
                [qa, research],  # QA can communicate with Research for corrections
                [qa, writer],  # QA can communicate with Writer for corrections
                [qa, designer],  # QA can communicate with Designer for corrections
            ],
            shared_instructions="agency_manifesto.md",
            temperature=0.7,
            max_prompt_tokens=4000
        )

    def interactive_chat(self, initial_task: str = None):
        """
        Run the agency with user interaction controls.
        """
        try:
            # Start the demo chat with initial task
            print("\nStarting interactive chat. Press Ctrl+C to exit gracefully.")
            print("\nInitial task:", initial_task)

            while True:
                try:
                    # Run one iteration of the demo chat
                    self.run_demo()  # run_demo() doesn't return a value

                    # Save intermediate results after each step
                    current_agent = self.current_agent if hasattr(
                        self, 'current_agent') else None
                    if current_agent:
                        self.results_manager.save_result(
                            current_agent.name,
                            "interaction",
                            {"agent_name": current_agent.name}
                        )

                    # Ask for user feedback
                    print("\nOptions:")
                    print("1. Continue")
                    print("2. Provide feedback")
                    print("3. Terminate")
                    choice = input("Choose an option (1-3): ")

                    if choice == "2":
                        feedback = input("Please provide your feedback: ")
                        # Save feedback
                        self.results_manager.save_result(
                            "user",
                            "feedback",
                            {"feedback": feedback}
                        )
                        print("\nPlease enter this feedback in the chat above ↑")
                    elif choice == "3":
                        print("Terminating agency...")
                        # Save final state
                        self.results_manager.save_result(
                            "agency",
                            "termination",
                            {"status": "user_terminated"}
                        )
                        break

                except Exception as e:
                    print(f"\nError in chat iteration: {str(e)}")
                    self.results_manager.save_result(
                        "agency",
                        "error",
                        {"error": str(e)}
                    )
                    choice = input("\nDo you want to continue? (y/n): ")
                    if choice.lower() != 'y':
                        break

        except KeyboardInterrupt:
            print("\nGracefully handling interruption...")
            # Save state on interruption
            self.results_manager.save_result(
                "agency",
                "termination",
                {"status": "interrupted"}
            )
        except Exception as e:
            print(f"\nError occurred: {str(e)}")
            # Save error state
            self.results_manager.save_result(
                "agency",
                "error",
                {"error": str(e)}
            )
            raise
        finally:
            print("Agency session completed. Results saved.")


if __name__ == "__main__":
    # Ensure input and output directories exist
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # Create and start the agency
    agency = PresentationAgency()

    # List PDF files in input directory
    pdf_files = [f for f in os.listdir("input") if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the input directory.")
        print("Please place a PDF file in the input directory.")
        exit(1)

    # Use the first PDF file found
    pdf_file = pdf_files[0]
    print(f"\nFound PDF file: {pdf_file}")

    # Show the proposed task
    print("\nProposed task:")
    print("-" * 80)
    task = f"""Please create a 5-minute PowerPoint presentation in Portuguese about throughput estimation based on the PDF file '{pdf_file}'.

IMPORTANT: Use the PDFReader tool with exactly this file path: '{pdf_file}'

The presentation should:
1. Extract key information from the PDF
2. Translate content to Portuguese
3. Include formulas and explanations
4. Create relevant graphs
5. Be saved in the output directory as 'throughput_presentation.pptx'"""
    print(task)
    print("-" * 80)

    # Start the interactive chat
    agency.interactive_chat(task)
