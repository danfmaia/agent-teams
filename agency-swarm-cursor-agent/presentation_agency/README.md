# Portuguese PowerPoint Presentation Agency

An Agency Swarm–based system that creates professional PowerPoint presentations in Portuguese about throughput estimation from PDF articles.

## Overview

This agency uses a team of specialized AI agents to:

1. Extract information from technical PDF articles
2. Translate and adapt content to Portuguese
3. Create professional PowerPoint presentations
4. Ensure quality and accuracy through review

## Project Structure

```
presentation_agency/
├── input/                  # Place PDF articles here
├── output/                 # Generated presentations are saved here
├── results/               # Intermediary results and agent interactions
├── ResearchAgent/         # PDF analysis and information extraction
├── ContentWriter/         # Translation and content adaptation
├── PresentationDesigner/  # PowerPoint creation and formatting
├── QAAgent/              # Quality assurance and review
├── agency.py             # Main agency configuration
├── agency_manifesto.md   # Shared instructions for all agents
└── requirements.txt      # Project dependencies
```

## Requirements

- Python 3.11 or higher
- OpenAI API key (set in `.env` file)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd presentation_agency
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Place your PDF article about throughput estimation in the `input/` directory.

2. Run the agency:

```bash
python agency.py
```

3. The agency will:

   - Read the PDF article
   - Extract key information
   - Translate content to Portuguese
   - Create a PowerPoint presentation
   - Save the presentation in the `output/` directory

4. During execution, you can:
   - Continue the process
   - Provide feedback
   - Terminate gracefully

## Agent Roles

- **Research Agent**: Analyzes PDF articles and extracts key information
- **Content Writer**: Translates and adapts content to Portuguese
- **Presentation Designer**: Creates and formats PowerPoint presentations
- **QA Agent**: Reviews for accuracy, clarity, and language quality

## Features

- PDF text extraction
- Portuguese translation with technical accuracy
- Professional PowerPoint creation
- Mathematical formula formatting
- Graph and visualization generation
- Quality assurance review
- Progress saving and recovery
- Interactive user feedback

## Results Management

The agency saves all intermediary results in the `results/` directory, organized by:

- Timestamp-based sessions
- Agent-specific outputs
- Stage-based progress
- User feedback and interactions

## Error Handling

- Graceful interruption handling
- Automatic result saving
- Error state recovery
- User feedback integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your chosen license]

## Acknowledgments

- Built with [Agency Swarm](https://github.com/VRSEN/agency-swarm)
- Uses OpenAI's GPT-4 for intelligence
