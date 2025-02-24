from langchain.tools import BaseTool
import PyPDF2
from typing import Optional


class DocumentTools:
    @staticmethod
    def pdf_reader() -> BaseTool:
        def read_pdf(file_path: str) -> str:
            """Read and extract text from a PDF file"""
            try:
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                    return text
            except Exception as e:
                return f"Error reading PDF: {str(e)}"

        return BaseTool(
            name="PDF Reader",
            func=read_pdf,
            description="Reads and extracts text from a PDF file"
        )
