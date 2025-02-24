import re
from typing import Dict

from langchain.schema import HumanMessage

from .base_agent import BaseAgent


class TranslationAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "Translation Agent"
        self.description = "translating technical content to Portuguese while maintaining accuracy"

    def _create_translation_prompt(self, text: str) -> str:
        return f"""Translate the following technical text to Portuguese.
                  Maintain all technical terms accurate and preserve mathematical formulas.
                  If you encounter specialized technical terms, provide both the Portuguese translation
                  and the original English term in parentheses.

                  Text to translate:
                  {text}"""

    async def _translate_section(self, section: Dict[str, str]) -> Dict[str, str]:
        """Translate a single section while preserving technical accuracy"""
        self.logger.info(f"Translating section: {section['title']}")

        messages = [
            HumanMessage(content=self._create_translation_prompt(
                section["content"]))
        ]

        response = await self.llm.ainvoke(messages)

        title_prompt = f"Translate this title to Portuguese: {section['title']}"
        title_response = await self.llm.ainvoke([HumanMessage(content=title_prompt)])

        self.logger.info(
            f"Completed translation for section: {section['title']}")
        return {
            "title": title_response.content,
            "content": response.content
        }

    async def process(self, state: Dict) -> Dict:
        """Translate the PDF content to Portuguese"""
        try:
            self.logger.info("Starting content translation")

            if "pdf_content" not in state:
                raise ValueError("No PDF content found in state")

            pdf_content = state["pdf_content"]

            # Translate sections
            self.logger.info(
                f"Translating {len(pdf_content['sections'])} sections")
            translated_sections = []
            technical_terms = {}

            for section in pdf_content["sections"]:
                translated_section = await self._translate_section(section)
                translated_sections.append(translated_section)

                # Extract technical terms (terms in parentheses)
                terms = re.findall(r'\(([^)]+)\)',
                                   translated_section["content"])
                for term in terms:
                    if " - " in term:
                        pt, en = term.split(" - ")
                        technical_terms[en.strip()] = pt.strip()

            # Update state
            state["translated_content"] = {
                "sections": translated_sections,
                # Formulas remain unchanged
                "formulas": pdf_content["formulas"],
                "technical_terms": technical_terms
            }

            state["status"] = "Content translated"
            state["current_agent"] = "Presentation Designer Agent"

            self.logger.success(
                f"Successfully translated content with {len(technical_terms)} technical terms")

        except Exception as e:
            self.logger.error(f"Error in translation: {str(e)}")
            state["errors"].append(f"Translation Agent error: {str(e)}")
            state["status"] = "Error in translation"

        return state
