from agency_swarm import Agent


class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            description="Responsible for reading and analyzing PDF documents about throughput estimation.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=25000,
        )
