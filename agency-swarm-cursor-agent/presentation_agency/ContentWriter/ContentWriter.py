from agency_swarm import Agent
from results_manager import ResultsManager


class ContentWriter(Agent):
    def __init__(self):
        # Initialize results manager
        self.results_manager = ResultsManager()

        super().__init__(
            name="Content Writer",
            description="Adapts and translates content into Portuguese, ensuring technical accuracy and presentation suitability",
            instructions="./instructions.md",
            tools=[],
            temperature=0.5,
            max_prompt_tokens=32000,
            model="gpt-4o"
        )

    def response_validator(self, message):
        """
        Validate and process the response before sending it to the next agent.
        Ensures content is properly saved and structured.
        """
        try:
            # Save the translated content
            self.results_manager.save_result(
                "ContentWriter",
                "translation",
                {
                    "slides": self._extract_slides_from_message(message),
                    "original_message": message
                }
            )
            return message
        except Exception as e:
            print(f"Warning: Failed to save content: {str(e)}")
            return message

    def _extract_slides_from_message(self, message: str) -> dict:
        """
        Extract structured slide content from the message.
        This is a simple implementation - you might want to make it more robust.
        """
        slides = {}
        current_slide = None
        content = []

        for line in message.split('\n'):
            if 'Slide' in line and ':' in line:
                # If we were building a previous slide, save it
                if current_slide is not None:
                    slides[current_slide] = '\n'.join(content)
                # Start a new slide
                current_slide = line.split(':')[0].strip()
                content = []
            elif current_slide is not None:
                content.append(line.strip())

        # Save the last slide if exists
        if current_slide is not None and content:
            slides[current_slide] = '\n'.join(content)

        return slides
