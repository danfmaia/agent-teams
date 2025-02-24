import json
import os
from typing import Dict, List

from langchain_anthropic import ChatAnthropic

from utils.logging import AgentLogger


class BaseAgent:
    def __init__(self, model_name: str = "claude-3-sonnet-20241022"):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is not set")
        self.llm = ChatAnthropic(model=model_name, anthropic_api_key=api_key)
        self.name = "base_agent"
        self.description = "Base agent class"
        self.logger = AgentLogger(self.name)

    def _format_message(self, content: str, role: str = "human") -> Dict:
        return {"role": role, "content": content}

    def _get_chat_history(self, messages: List[Dict]) -> str:
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    def _create_system_prompt(self, context: Dict) -> str:
        return f"""You are {self.name}, a specialized AI agent responsible for {self.description}.
                  Current context: {json.dumps(context, indent=2)}

                  Follow these guidelines:
                  1. Focus on your specific role and responsibilities
                  2. Maintain high accuracy and quality
                  3. Consider the overall presentation flow
                  4. Use appropriate technical terminology
                  5. Keep the 5-minute time constraint in mind"""

    async def process(self, state: Dict) -> Dict:
        """Process the current state and return updated state"""
        raise NotImplementedError("Subclasses must implement process method")
