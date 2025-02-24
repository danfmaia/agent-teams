from agency_swarm import Agent
from .tools import PDFReader


class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            description="Analyzes PDF articles and extracts key information about throughput estimation",
            instructions="./instructions.md",
            tools=[PDFReader],
            temperature=0.5,
            max_prompt_tokens=32000,
            model="gpt-4o"
        )

    def response_validator(self, message):
        return message
