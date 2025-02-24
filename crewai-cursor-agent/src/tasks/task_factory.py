from typing import Dict, Any, List
from crewai import Task, Agent
from agents.agent_templates import AgentTemplates


class TaskFactory:
    """Factory class for creating dynamic tasks based on user specifications"""

    @staticmethod
    def create_task(
        description: str,
        agent: Agent,
        tools: List[callable] = None,
        context: Dict[str, Any] = None,
        dependencies: List[Task] = None
    ) -> Task:
        """
        Create a new task with specified parameters

        Args:
            description: Detailed description of the task
            agent: The agent assigned to this task
            tools: List of tools available for this task
            context: Additional context/data for the task
            dependencies: Tasks that must be completed before this one
        """
        return Task(
            description=description,
            agent=agent,
            tools=tools or [],
            context=context or {},
            dependencies=dependencies or []
        )

    @staticmethod
    def parse_task_description(task_input: str) -> Dict[str, Any]:
        """
        Parse a natural language task description into structured components

        Args:
            task_input: Natural language description of the task

        Returns:
            Dictionary containing parsed task components
        """
        # This is a placeholder for more sophisticated task parsing
        return {
            "description": task_input,
            "required_tools": [],
            "suggested_agent_type": "planner"  # Default to planner for initial task breakdown
        }

    @staticmethod
    def create_presentation_tasks(pdf_path: str) -> List[Task]:
        # Get our agents
        researcher = AgentTemplates.create_research_agent()
        creator = AgentTemplates.create_presentation_creator()
        translator = AgentTemplates.create_translator()
        reviewer = AgentTemplates.create_reviewer()

        tasks = [
            Task(
                description=f"""
                1. Read and analyze the PDF file at {pdf_path}
                2. Extract key information about Throughput estimation
                3. Identify important formulas, methodologies, and results
                4. Create a structured outline for the presentation
                5. Prepare data for visualization
                """,
                agent=researcher,
                expected_output="A comprehensive analysis with key points, formulas, and data for the presentation",
                context="This research will form the foundation of our presentation"
            ),

            Task(
                description="""
                1. Create a 5-minute PowerPoint presentation using the research findings
                2. Include clear explanations of formulas and concepts
                3. Create appropriate graphs and visualizations
                4. Ensure logical flow and professional formatting
                5. Design slides for maximum impact within the 5-minute constraint
                """,
                agent=creator,
                expected_output="A draft PowerPoint presentation with all key elements included",
                context="The presentation should be engaging and professional"
            ),

            Task(
                description="""
                1. Translate all presentation content to Portuguese
                2. Ensure technical terms are correctly translated
                3. Maintain the precision of mathematical and technical concepts
                4. Adapt any cultural references appropriately
                5. Verify natural flow in Portuguese
                """,
                agent=translator,
                expected_output="A fully translated presentation in Portuguese",
                context="The translation must maintain technical accuracy while being natural in Portuguese"
            ),

            Task(
                description="""
                1. Review the entire presentation for technical accuracy
                2. Verify the clarity of explanations and visualizations
                3. Check the translation quality and consistency
                4. Ensure the presentation fits within 5 minutes
                5. Suggest improvements for clarity and impact
                """,
                agent=reviewer,
                expected_output="A detailed review with specific improvement suggestions",
                context="The final presentation must be polished and professional"
            )
        ]

        return tasks
