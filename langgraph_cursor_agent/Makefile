# Conda environment management
CONDA_ENV_NAME := langgraph_agent
PYTHON_VERSION := 3.10
SHELL := /bin/bash

.PHONY: help create-env remove-env install-deps install-dev update-deps activate-env clean

help:
	@echo "Makefile commands:"
	@echo "create-env    : Create conda environment with Python $(PYTHON_VERSION)"
	@echo "remove-env    : Remove conda environment"
	@echo "install-deps  : Install project dependencies"
	@echo "install-dev   : Install development dependencies"
	@echo "update-deps   : Update project dependencies"
	@echo "activate-env  : Activate conda environment"
	@echo "clean        : Clean cache files"

create-env:
	conda create -n $(CONDA_ENV_NAME) python=$(PYTHON_VERSION) -y
	@echo "To activate the environment, run: conda activate $(CONDA_ENV_NAME)"

remove-env:
	conda env remove -n $(CONDA_ENV_NAME) -y

install-deps:
	@echo "Installing dependencies..."
	conda run -n $(CONDA_ENV_NAME) pip install -e .

install-dev:
	@echo "Installing development dependencies..."
	conda run -n $(CONDA_ENV_NAME) pip install -e ".[dev]"

update-deps:
	@echo "Updating dependencies..."
	conda run -n $(CONDA_ENV_NAME) pip install -e . --upgrade

activate-env:
	@echo "To activate the environment, run: conda activate $(CONDA_ENV_NAME)"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".DS_Store" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +
	find . -type d -name ".hypothesis" -exec rm -rf {} + 