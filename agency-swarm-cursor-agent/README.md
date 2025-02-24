# Cursor Agent Tutorial

A tutorial project demonstrating how to build AI agent teams using Agency Swarm framework in Cursor IDE. This project showcases the creation of specialized AI agents that collaborate to accomplish complex tasks.

## Project Overview

This repository contains a practical example of building an AI agent team that creates PowerPoint presentations. The example demonstrates:

- Building multi-agent systems with Agency Swarm
- Agent communication and collaboration
- Tool development and integration
- Error handling and result management
- User interaction and feedback loops

## Repository Structure

```
cursor-agent-tutorial/
├── agency-swarm/            # Agency Swarm framework documentation and rules
├── presentation_agency/     # Main example agency implementation
│   ├── input/              # Input files for the agency
│   ├── output/             # Generated presentations
│   ├── results/            # Intermediary results
│   ├── runs/               # Execution run logs
│   ├── ResearchAgent/      # PDF analysis agent
│   ├── ContentWriter/      # Translation agent
│   ├── PresentationDesigner/ # PowerPoint creation agent
│   ├── QAAgent/            # Quality assurance agent
│   ├── agency.py          # Main agency configuration
│   ├── agency_manifesto.md # Shared instructions for all agents
│   └── README.md           # Agency-specific documentation
├── presentation_agency_1/   # Alternative implementation
├── input/                  # Shared input files for all implementations
├── .vscode/                # VS Code/Cursor IDE configuration
├── .pylintrc              # Python linting configuration
├── .cursorrules           # Cursor IDE specific rules
└── README.md              # This file
```

## Tutorial Steps

1. **Agency Planning**

   - Define agency purpose and requirements
   - Design agent roles and responsibilities
   - Plan communication flows
   - Identify required tools and APIs

2. **Project Setup**

   - Create agency and agent templates
   - Set up folder structure
   - Configure environment variables
   - Install dependencies

3. **Tool Development**

   - Create specialized tools for each agent
   - Implement error handling
   - Add validation and testing
   - Document tool usage

4. **Agent Implementation**

   - Define agent instructions
   - Configure agent parameters
   - Set up tool integration
   - Implement response validation

5. **Agency Integration**
   - Configure communication flows
   - Set up result management
   - Implement user interaction
   - Add error recovery

## Key Features

- **Modular Design**: Each agent is a self-contained module with clear responsibilities
- **Robust Error Handling**: Graceful handling of interruptions and errors
- **Result Management**: Structured storage of intermediary results
- **User Interaction**: Interactive feedback and control mechanisms
- **Documentation**: Comprehensive documentation at all levels

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cursor-agent-tutorial.git
cd cursor-agent-tutorial
```

2. Follow the README in the `presentation_agency` directory for specific implementation details.

## Prerequisites

- [Cursor IDE](https://cursor.sh/)
- Python 3.11 or higher
- OpenAI API key
- Agency Swarm framework

## Learning Resources

- [Agency Swarm Documentation](https://github.com/VRSEN/agency-swarm)
- [Cursor IDE Documentation](https://cursor.sh/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Acknowledgments

- [Agency Swarm](https://github.com/VRSEN/agency-swarm) for the multi-agent framework
- [Cursor](https://cursor.sh/) for the AI-powered IDE
- OpenAI for the GPT models powering the agents
