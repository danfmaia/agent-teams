# Automated Presentation Generator

This application automatically generates a 5-minute PowerPoint presentation in Portuguese about Throughput Estimation from a technical PDF article. The system uses a team of specialized AI agents to handle different aspects of the presentation creation process.

## Features

- PDF content extraction and analysis
- Professional Portuguese translation with technical accuracy
- Automatic PowerPoint generation with formulas and graphs
- Quality review and improvement process
- Real-time progress tracking
- Beautiful Streamlit interface

## Agent Team

1. **PDF Reader Agent**: Extracts and structures content from technical PDFs
2. **Translation Agent**: Translates content to Portuguese while maintaining technical accuracy
3. **Presentation Designer Agent**: Creates and formats the PowerPoint presentation
4. **Review Agent**: Reviews content for accuracy, grammar, and timing
5. **Improvement Agent**: Implements improvements based on review feedback

## Requirements

- Python 3.10+
- Conda package manager
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate the conda environment:

```bash
# Create environment
make create-env

# Activate environment
conda activate langgraph_agent
```

3. Install dependencies:

```bash
make install-deps
```

## Development

The project includes several development tools:

- **pytest**: For running tests
- **black**: For code formatting
- **flake8**: For code linting
- **mypy**: For type checking
- **isort**: For import sorting

To update dependencies:

```bash
make update-deps
```

To clean cache files:

```bash
make clean
```

## Usage

1. Start the Streamlit app:

```bash
streamlit run src/app.py
```

2. Upload your technical PDF article about Throughput Estimation

3. Click "Generate Presentation" to start the process

4. Monitor the progress in real-time through the interface

5. Download the generated presentation when complete

## Project Structure

```
.
├── input/              # Directory for uploaded PDF files
├── output/             # Directory for generated presentations
├── src/
│   ├── agents/        # Individual agent implementations
│   ├── utils/         # Utility functions and types
│   ├── app.py         # Streamlit application
│   └── workflow.py    # LangGraph workflow definition
├── requirements.txt    # Project dependencies
├── Makefile          # Build and environment management
└── README.md          # This file
```

## Technical Details

- Built with LangChain and LangGraph for agent orchestration
- Uses Claude 3-5 Sonnet for AI capabilities
- Implements modular architecture for easy maintenance
- Features state management between agent nodes
- Includes error handling and recovery

## Notes

- The presentation is optimized for a 5-minute delivery time
- Technical terms are preserved in both English and Portuguese
- The system includes multiple review cycles for quality assurance
- Progress and agent status are displayed in real-time
