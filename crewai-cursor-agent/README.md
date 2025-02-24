# Throughput Estimation Presentation Creator

An AI-powered application that creates professional PowerPoint presentations about Throughput estimation from PDF articles. The application uses a team of specialized AI agents to analyze, create, translate, and review the presentation.

## Features

- PDF article analysis
- Automatic PowerPoint presentation creation
- Portuguese translation
- Formula and graph visualization
- Professional review and improvement

## Prerequisites

- Python 3.10 or higher
- Conda package manager
- Make (usually pre-installed on Linux/Mac, for Windows install via chocolatey)

## Installation and Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate the Conda environment:

```bash
# Create the environment and install dependencies
make env-create

# If you're using Windows PowerShell, activate the environment with:
conda activate crewai-cursor-agent

# If you're using Linux/Mac, activate with:
source activate crewai-cursor-agent
```

3. Environment Management:

```bash
# Update dependencies in existing environment
make env-update

# Export current environment to requirements.txt
make env-export

# Clean up cache and build files
make clean
```

## Usage

1. Start the Streamlit application:

```bash
make run
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload your PDF article about Throughput estimation

4. Click "Create Presentation" and wait for the AI agents to:

   - Analyze the PDF
   - Create the presentation
   - Translate to Portuguese
   - Review and improve the content

5. Download the final presentation when ready

## Development

### Code Quality

```bash
# Run linters (pylint and flake8)
make lint

# Run tests
make test
```

### Available Make Commands

- `make env-create`: Create new Conda environment with dependencies
- `make env-update`: Update existing environment
- `make env-export`: Export current dependencies to requirements.txt
- `make clean`: Clean up Python cache and build files
- `make run`: Run the Streamlit application
- `make lint`: Run code linters
- `make test`: Run tests
- `make help`: Show all available commands

## Agent Team

The application uses four specialized AI agents:

1. **Research and Analysis Specialist**

   - Analyzes the PDF article
   - Extracts key information
   - Identifies formulas and data for visualization

2. **PowerPoint Presentation Specialist**

   - Creates professional slides
   - Implements visualizations
   - Ensures clear communication

3. **Technical Translator**

   - Translates content to Portuguese
   - Maintains technical accuracy
   - Ensures natural language flow

4. **Quality Assurance Specialist**
   - Reviews technical accuracy
   - Verifies translation quality
   - Suggests improvements

## Dependencies

Key dependencies include:

- crewai==0.16.2: Core agent framework
- anthropic==0.38.0: Claude AI model integration
- streamlit==1.39.0: Web interface
- langchain==0.1.12: Language model tools
- python-pptx==0.6.23: PowerPoint generation
- PyPDF2==3.0.1: PDF processing

For a complete list of dependencies, see `requirements.txt`

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

## Troubleshooting

If you encounter import errors after creating the environment:

1. Ensure you've activated the Conda environment
2. Try updating the environment: `make env-update`
3. Check if all dependencies are installed: `conda list -n crewai-cursor-agent`

## License

MIT License
