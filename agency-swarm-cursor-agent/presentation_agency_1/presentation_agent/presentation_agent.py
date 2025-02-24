from agency_swarm import Agent


class PresentationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Presentation Creator",
            description="Responsible for creating PowerPoint presentations in Portuguese about throughput estimation.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.7,
            max_prompt_tokens=25000,
        )
