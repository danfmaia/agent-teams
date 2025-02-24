import re
from pathlib import Path
from typing import Dict, List

import PyPDF2

from .base_agent import BaseAgent


class PDFReaderAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "PDF Reader Agent"
        self.description = "extracting and structuring content from technical PDF articles"

    def _extract_formulas(self, text: str) -> List[str]:
        """Extract mathematical formulas from text"""
        # Basic formula detection (can be enhanced)
        formula_patterns = [
            r'\$.*?\$',  # LaTeX inline formulas
            r'\\\[.*?\\\]',  # LaTeX display formulas
            r'[a-zA-Z\d]+\s*=\s*[^.]+',  # Simple equations
        ]
        formulas = []
        for pattern in formula_patterns:
            formulas.extend(re.findall(pattern, text))
        return formulas

    def _extract_data_for_graphs(self, text: str) -> List[Dict]:
        """Identify potential data that could be visualized"""
        # This is a placeholder - in real implementation, we'd use more sophisticated methods
        data_sections = []

        # Look for sections with numerical data
        number_dense_paragraphs = [p for p in text.split('\n\n')
                                   if len(re.findall(r'\d+\.?\d*', p)) > 5]

        for paragraph in number_dense_paragraphs:
            data_sections.append({
                "type": "potential_graph",
                "content": paragraph,
                "numbers": re.findall(r'\d+\.?\d*', paragraph)
            })

        return data_sections

    async def process(self, state: Dict) -> Dict:
        """Process the PDF and extract structured content"""
        try:
            self.logger.info("Starting PDF processing")

            pdf_path = Path("input/article.pdf")
            if not pdf_path.exists():
                raise FileNotFoundError(f"PDF file not found at {pdf_path}")

            # Read PDF
            self.logger.info("Reading PDF file")
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

            # Extract content
            self.logger.info("Extracting formulas and data")
            formulas = self._extract_formulas(text)
            data_for_graphs = self._extract_data_for_graphs(text)

            # Structure content into sections
            self.logger.info("Structuring content into sections")
            sections = []
            current_section = {"title": "", "content": ""}
            for line in text.split('\n'):
                if re.match(r'^[0-9]+\.|^[A-Z\s]{3,}$', line.strip()):
                    if current_section["title"]:
                        sections.append(current_section.copy())
                    current_section = {"title": line.strip(), "content": ""}
                else:
                    current_section["content"] += line + "\n"

            if current_section["title"]:
                sections.append(current_section)

            # Update state
            state["pdf_content"] = {
                "text": text,
                "formulas": formulas,
                "data_for_graphs": data_for_graphs,
                "sections": sections
            }
            state["status"] = "PDF content extracted"
            state["current_agent"] = "Translation Agent"

            self.logger.success(
                f"Successfully processed PDF with {len(sections)} sections")

        except FileNotFoundError as e:
            self.logger.error(f"PDF file not found: {str(e)}")
            state["errors"].append(f"PDF Reader Agent error: {str(e)}")
            state["status"] = "Error in PDF processing"
        except Exception as e:
            self.logger.error(f"Error processing PDF: {str(e)}")
            state["errors"].append(f"PDF Reader Agent error: {str(e)}")
            state["status"] = "Error in PDF processing"

        return state
