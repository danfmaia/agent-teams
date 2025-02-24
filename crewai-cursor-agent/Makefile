.PHONY: env env-create env-update clean run test lint

# Environment variables
CONDA_ENV_NAME=crewai-cursor-agent
PYTHON_VERSION=3.10
SHELL=/bin/bash

# Conda environment management
env-create:
	@echo "Creating Conda environment: $(CONDA_ENV_NAME)..."
	@conda create -n $(CONDA_ENV_NAME) python=$(PYTHON_VERSION) -y
	@echo "Activating environment and installing dependencies..."
	@conda run -n $(CONDA_ENV_NAME) pip install -r requirements.txt

env-update:
	@echo "Updating Conda environment: $(CONDA_ENV_NAME)..."
	@conda run -n $(CONDA_ENV_NAME) pip install -r requirements.txt

env-export:
	@echo "Exporting Conda environment to requirements.txt..."
	@conda run -n $(CONDA_ENV_NAME) pip freeze > requirements.txt

clean:
	@echo "Cleaning up Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@find . -type f -name ".DS_Store" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name "*.egg" -delete
	@rm -rf build/
	@rm -rf dist/
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@echo "Cleanup complete!"

run:
	@echo "Running Streamlit app..."
	@conda run -n $(CONDA_ENV_NAME) streamlit run src/app.py

lint:
	@echo "Running linters..."
	@conda run -n $(CONDA_ENV_NAME) pylint src/
	@conda run -n $(CONDA_ENV_NAME) flake8 src/

test:
	@echo "Running tests..."
	@conda run -n $(CONDA_ENV_NAME) pytest tests/

# Default target
all: env-create

# Help target
help:
	@echo "Available targets:"
	@echo "  env-create  : Create a new Conda environment and install dependencies"
	@echo "  env-update  : Update existing Conda environment with dependencies"
	@echo "  env-export  : Export current environment to requirements.txt"
	@echo "  clean      : Clean up Python cache and build files"
	@echo "  run        : Run the Streamlit application"
	@echo "  lint       : Run code linters"
	@echo "  test       : Run tests"
	@echo "  help       : Show this help message" 