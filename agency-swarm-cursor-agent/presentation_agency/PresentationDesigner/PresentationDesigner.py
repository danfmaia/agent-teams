from agency_swarm import Agent
from .tools import PPTXCreator
from results_manager import ResultsManager


class PresentationDesigner(Agent):
    def __init__(self):
        # Initialize results manager
        self.results_manager = ResultsManager()

        super().__init__(
            name="Presentation Designer",
            description="Creates and formats PowerPoint presentations with proper formatting, formulas, and graphs",
            instructions="./instructions.md",
            tools=[PPTXCreator],
            temperature=0.7,
            max_prompt_tokens=4000
        )

    def response_validator(self, message):
        """
        Process the message and create the presentation using saved content.
        """
        try:
            # Load the latest translated content
            content_data = self.results_manager.load_latest_result(
                "ContentWriter", "translation")

            if not content_data or 'slides' not in content_data.get('data', {}):
                print("Warning: No translated content found")
                return message

            slides = content_data['data']['slides']

            # Prepare content for PPTXCreator
            presentation_content = {}
            for slide_num, (slide_title, content) in enumerate(slides.items(), 1):
                # Extract any graph data if present (this is a simple implementation)
                graph_data = None
                if "gráfico" in content.lower() or "graph" in content.lower():
                    # You might want to implement more sophisticated graph data extraction
                    graph_data = {
                        "x": [1, 2, 3, 4, 5],
                        "y": [2, 4, 6, 8, 10],
                        "title": "Sample Graph",
                        "xlabel": "X",
                        "ylabel": "Y"
                    }

                presentation_content[slide_num] = {
                    "title": slide_title.replace("Slide", "").strip(),
                    "content": content,
                    "graph_data": graph_data
                }

            # Save the presentation structure
            self.results_manager.save_result(
                "PresentationDesigner",
                "structure",
                {"content": presentation_content}
            )

            # Create the presentation
            creator = PPTXCreator(
                content=presentation_content,
                output_filename="throughput_presentation.pptx"
            )
            result = creator.run()

            # Save the creation result
            self.results_manager.save_result(
                "PresentationDesigner",
                "creation",
                {"status": result}
            )

            return message
        except Exception as e:
            print(f"Warning: Failed to create presentation: {str(e)}")
            return message
