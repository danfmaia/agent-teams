from pydantic import Field
import os
from dotenv import load_dotenv
import PyPDF2
import re

load_dotenv()


class PDFReader:
    """
    A tool for reading and extracting information from PDF files.
    It can extract text, formulas, and identify potential areas for graphs.
    """

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def run(self):
        """
        Reads the PDF file and extracts its content, including text and potential formulas.
        Returns a structured dictionary with the extracted information.
        """
        try:
            # Get the absolute path to the PDF file
            base_dir = os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))
            full_pdf_path = os.path.join(base_dir, self.pdf_path)

            print(f"Attempting to read PDF from: {full_pdf_path}")

            if not os.path.exists(full_pdf_path):
                return f"Error: PDF file not found at {full_pdf_path}"

            with open(full_pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                content = []
                formulas = []
                key_sections = {
                    'abstract': '',
                    'introduction': '',
                    'methodology': '',
                    'results': '',
                    'conclusion': ''
                }
                current_section = None

                for page in pdf_reader.pages:
                    text = page.extract_text()

                    # Detect section headers
                    lower_text = text.lower()
                    if 'abstract' in lower_text[:100]:
                        current_section = 'abstract'
                    elif 'introduction' in lower_text or 'introdução' in lower_text:
                        current_section = 'introduction'
                    elif 'methodology' in lower_text or 'metodologia' in lower_text:
                        current_section = 'methodology'
                    elif 'results' in lower_text or 'resultados' in lower_text:
                        current_section = 'results'
                    elif 'conclusion' in lower_text or 'conclusão' in lower_text:
                        current_section = 'conclusion'

                    # Store content in appropriate section
                    if current_section:
                        key_sections[current_section] += text

                    # Detect formulas (improved pattern)
                    formula_patterns = [
                        # Basic equations
                        r'[A-Za-z]+\s*=\s*[A-Za-z0-9\+\-\*/\(\)]+',
                        r'[A-Za-z]+\s*\([A-Za-z,\s]+\)\s*=',  # Functions
                        r'∑|∫|∂|√|π|λ|μ|σ|α|β|γ|θ'  # Mathematical symbols
                    ]

                    for pattern in formula_patterns:
                        found_formulas = re.findall(pattern, text)
                        if found_formulas:
                            formulas.extend(found_formulas)

                # Remove duplicates from formulas
                formulas = list(set(formulas))

                # Filter out non-mathematical formulas
                formulas = [f for f in formulas if any(
                    char in f for char in '=+-*/()∑∫∂√πλμσαβγθ')]

                return {
                    'sections': key_sections,
                    # Limit to top 10 most relevant formulas
                    'formulas': formulas[:10],
                    'num_pages': len(pdf_reader.pages)
                }

        except Exception as e:
            return f"Error reading PDF: {str(e)}"


if __name__ == "__main__":
    # Test the tool
    tool = PDFReader(pdf_path="input/06170058.pdf")
    result = tool.run()
    if isinstance(result, dict):
        print(f"Number of pages: {result['num_pages']}")
        print("\nSections found:")
        for section, content in result['sections'].items():
            print(f"\n{section.upper()}:")
            print(content[:200] + "..." if content else "Not found")
        print("\nFormulas found:", result['formulas'])
    else:
        print("Error:", result)
