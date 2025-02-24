from agency_swarm.tools import BaseTool
from pydantic import Field
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()


class PDFReader(BaseTool):
    """
    A tool for reading and extracting information from PDF files.
    It can read PDF files from the input folder and extract text content.
    """

    file_path: str = Field(
        ..., description="The name of the PDF file to read (e.g., 'document.pdf')"
    )

    def run(self):
        """
        Reads the specified PDF file and returns its text content.
        """
        # Try different path combinations
        possible_paths = [
            self.file_path,  # Try direct path
            os.path.join('input', self.file_path),  # Try in input directory
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
                __file__))), 'input', self.file_path)  # Try absolute path
        ]

        for path in possible_paths:
            try:
                with open(path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text_content = ""

                    for page in pdf_reader.pages:
                        text_content += page.extract_text() + "\n"

                    return text_content
            except FileNotFoundError:
                continue
            except Exception as e:
                continue

        # If no path worked, return error with all attempted paths
        return f"Error: File {self.file_path} not found. Tried these locations:\n" + "\n".join(possible_paths)


if __name__ == "__main__":
    # Test the tool with a sample PDF
    tool = PDFReader(file_path="sample.pdf")
    print(tool.run())
