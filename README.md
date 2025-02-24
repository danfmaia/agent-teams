# Agent Teams

A collection of agent team implementations using different frameworks and approaches, all developed with Cursor's Agent feature. This repository serves as a portfolio demonstrating expertise in building and orchestrating AI agent teams for various use cases, showcasing the evolution from framework-less to framework-based implementations.

## Common Task: Presentation Generation

All four implementations tackle the same complex task: generating a 5-minute PowerPoint presentation about Throughput Estimation based on a research article. The task requirements include:

- Reading and analyzing a technical PDF article
- Creating a presentation in Portuguese
- Including mathematical formulas and graphs
- Providing clear explanations for all elements
- Implementing a review and improvement process

This common task allows for direct comparison of how different agent frameworks handle complex, multi-step processes requiring specialized knowledge and coordination.

## Projects Overview

### 1. No Framework Cursor Agent

The foundational project demonstrating agent team coordination without relying on any specific agentic framework. This bare-bones implementation showcases how basic agent collaboration patterns can be used to break down and execute complex presentation tasks.

Key features:

- Pure implementation of agent coordination
- Direct control over agent behaviors
- Minimal dependencies
- Custom tool integration for PDF processing and presentation generation

### 2. Agency Swarm Cursor Agent

Building upon the foundational concepts, this implementation leverages the Agency Swarm framework, introducing swarm-like behavior for distributed content generation and review processes.

Key features:

- Swarm intelligence principles for content organization
- File and directory management tools
- Requirements-based agent configuration
- Advanced PDF processing and analysis capabilities

### 3. CrewAI Cursor Agent

Advancing the agent collaboration approach, this project utilizes the CrewAI framework to create specialized agent roles for different aspects of presentation creation. CrewAI excels at creating hierarchical agent structures with clear responsibilities for research, content creation, and review.

Key features:

- Role-based agent teams (e.g., Researcher, Writer, Reviewer)
- Built-in tools for file operations and content processing
- Support for sequential and hierarchical processes
- Extensive tool ecosystem for presentation tasks

### 4. LangGraph Cursor Agent

The most sophisticated implementation, using LangChain's LangGraph framework to create a stateful workflow for presentation generation. LangGraph's directed graphs enable precise control over the presentation creation pipeline, from research to final review.

Key features:

- Graph-based orchestration of presentation workflow
- State management for tracking progress
- Checkpointing capabilities for long-running tasks
- Built-in support for streaming and persistence

## Development Approach

All projects in this repository follow a consistent development approach using Cursor's Agent feature and `.cursorrules` files. This approach provides:

- Standardized agent behavior definitions
- Consistent interaction patterns
- Reusable components across projects
- Clear separation of concerns

## Common Features Across Projects

- PDF analysis and information extraction
- Presentation generation and formatting
- Translation capabilities (English to Portuguese)
- Mathematical formula processing
- Graph generation
- Content review and improvement mechanisms
- File operations and management
- Tool-based architecture
- Error handling and recovery

## Getting Started

Each project has its own setup and requirements. Navigate to the specific project directory and follow the instructions in their respective README files.

## Technologies Used

- Python 3.x
- Various AI/ML frameworks (LangGraph, CrewAI, Agency Swarm)
- Cursor IDE and Agent feature
- Natural Language Processing tools
- PDF processing libraries
- Presentation generation tools
- Mathematical formula rendering
- Graph generation utilities
- Translation services

## Author

Daniel Maia - Full-Stack AI Engineer specializing in LLM/AI Engineering and Agentic AI development.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
