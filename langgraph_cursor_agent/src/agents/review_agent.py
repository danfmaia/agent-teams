from typing import Dict, List

from langchain.schema import HumanMessage

from .base_agent import BaseAgent


class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "Review Agent"
        self.description = "reviewing presentation content for accuracy and quality"

    def _create_review_prompt(self, slide: Dict[str, str], original_content: Dict) -> str:
        return f"""Review this presentation slide for accuracy and quality.
                  Compare it with the original content and evaluate:
                  1. Technical accuracy of the translation
                  2. Grammar and language quality
                  3. Presentation timing and flow
                  4. Clarity and organization

                  Slide content:
                  Title: {slide['title']}
                  Content: {slide['content']}

                  Original content:
                  {original_content}

                  Provide a score from 0.0 to 1.0 for each aspect and specific suggestions for improvement."""

    async def _review_slide(self, slide: Dict[str, str], original_content: Dict) -> List[str]:
        """Review a single slide and provide feedback"""
        self.logger.info(f"Reviewing slide: {slide['title']}")

        messages = [
            HumanMessage(content=self._create_review_prompt(
                slide, original_content))
        ]

        response = await self.llm.ainvoke(messages)
        feedback = response.content.split("\n")

        self.logger.info(f"Completed review for slide: {slide['title']}")
        return feedback

    async def process(self, state: Dict) -> Dict:
        """Review the presentation and provide feedback"""
        try:
            self.logger.info("Starting presentation review")

            if "presentation" not in state or "translated_content" not in state:
                raise ValueError(
                    "Missing presentation or translated content in state")

            presentation = state["presentation"]
            translated_content = state["translated_content"]

            # Review each slide
            self.logger.info(f"Reviewing {len(presentation['slides'])} slides")
            slide_feedback = {}
            total_accuracy = 0.0
            total_grammar = 0.0
            total_timing = 0.0

            for i, slide in enumerate(presentation["slides"]):
                feedback = await self._review_slide(slide, translated_content)
                slide_feedback[f"Slide {i+1}"] = feedback

                # Extract scores (assuming they're in the feedback)
                for line in feedback:
                    if "accuracy" in line.lower():
                        total_accuracy += float(line.split(":")[-1].strip())
                    elif "grammar" in line.lower():
                        total_grammar += float(line.split(":")[-1].strip())
                    elif "timing" in line.lower():
                        total_timing += float(line.split(":")[-1].strip())

            num_slides = len(presentation["slides"])
            avg_accuracy = total_accuracy / num_slides
            avg_grammar = total_grammar / num_slides
            avg_timing = total_timing / num_slides

            self.logger.info(
                f"Average scores - Accuracy: {avg_accuracy:.2f}, Grammar: {avg_grammar:.2f}, Timing: {avg_timing:.2f}")

            # Update state
            state["review_feedback"] = {
                "accuracy_score": avg_accuracy,
                "grammar_score": avg_grammar,
                "timing_score": avg_timing,
                "suggestions": [
                    "Improve technical term consistency",
                    "Add more visual elements",
                    "Balance content across slides"
                ],
                "slide_specific_feedback": slide_feedback
            }

            state["status"] = "Review completed"
            # Next agent will be determined by the workflow based on scores

            self.logger.success("Successfully completed presentation review")

        except Exception as e:
            self.logger.error(f"Error in review: {str(e)}")
            state["errors"].append(f"Review Agent error: {str(e)}")
            state["status"] = "Error in review"

        return state
