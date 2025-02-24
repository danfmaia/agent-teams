from crewai import Agent
from langchain_anthropic import ChatAnthropic
from tools.search_tools import SearchTools
from tools.document_tools import DocumentTools
from tools.presentation_tools import PresentationTools


class AgentTemplates:
    @staticmethod
    def create_research_agent() -> Agent:
        return Agent(
            role='Research and Analysis Specialist',
            goal='Extract and analyze key information about Throughput estimation from the provided PDF article',
            backstory="""You are an expert researcher with deep knowledge in technical analysis and data interpretation. 
            Your expertise lies in understanding complex technical concepts and identifying key information.""",
            tools=[DocumentTools.pdf_reader(), SearchTools.web_search()],
            llm=ChatAnthropic(model="claude-3-sonnet-20240229"),
            verbose=True
        )

    @staticmethod
    def create_presentation_creator() -> Agent:
        return Agent(
            role='PowerPoint Presentation Specialist',
            goal='Create a clear and engaging 5-minute PowerPoint presentation in Portuguese about Throughput estimation',
            backstory="""You are an expert in creating impactful presentations that effectively communicate complex technical concepts. 
            You excel at organizing information logically and creating visually appealing slides.""",
            tools=[PresentationTools.create_slide(
            ), PresentationTools.add_graph()],
            llm=ChatAnthropic(model="claude-3-sonnet-20240229"),
            verbose=True
        )

    @staticmethod
    def create_translator() -> Agent:
        return Agent(
            role='Technical Translator',
            goal='Ensure accurate translation of technical content from English to Portuguese while maintaining technical precision',
            backstory="""You are a specialized technical translator with expertise in engineering and technical documentation. 
            You ensure translations are both accurate and natural in Portuguese.""",
            tools=[],
            llm=ChatAnthropic(model="claude-3-sonnet-20240229"),
            verbose=True
        )

    @staticmethod
    def create_reviewer() -> Agent:
        return Agent(
            role='Quality Assurance Specialist',
            goal='Review and improve the presentation for technical accuracy, clarity, and effectiveness',
            backstory="""You are a detail-oriented reviewer with expertise in technical presentations. 
            You ensure all content is accurate, well-structured, and meets high-quality standards.""",
            tools=[DocumentTools.pdf_reader(
            ), PresentationTools.review_presentation()],
            llm=ChatAnthropic(model="claude-3-sonnet-20240229"),
            verbose=True
        )
