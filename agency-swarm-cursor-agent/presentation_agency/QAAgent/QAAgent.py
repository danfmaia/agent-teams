from agency_swarm import Agent
from .tools import PresentationReviewer


class QAAgent(Agent):
    def __init__(self):
        super().__init__(
            name="QA Agent",
            description="Reviews presentations for accuracy, clarity, and Portuguese language quality",
            instructions="./instructions.md",
            tools=[PresentationReviewer],
            temperature=0.7,
            max_prompt_tokens=4000
        )

    def response_validator(self, message):
        return message
