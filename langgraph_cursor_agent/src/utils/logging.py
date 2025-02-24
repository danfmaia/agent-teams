import logging
from pathlib import Path
from typing import Optional

import streamlit as st


def setup_logging(log_file: Optional[str] = None) -> logging.Logger:
    """Set up logging configuration"""
    # Create logger
    logger = logging.getLogger("presentation_generator")
    logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_formatter = logging.Formatter('%(levelname)s: %(message)s')

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(stream_formatter)
    logger.addHandler(console_handler)

    # Create file handler if log file specified
    if log_file:
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        file_handler = logging.FileHandler(log_dir / log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


def log_to_streamlit(message: str, level: str = "info") -> None:
    """Log message to Streamlit UI"""
    if level == "info":
        st.info(message)
    elif level == "success":
        st.success(message)
    elif level == "warning":
        st.warning(message)
    elif level == "error":
        st.error(message)

    # Add to session state messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append(f"[{level.upper()}] {message}")


class AgentLogger:
    """Logger class for agents with context"""

    def __init__(self, agent_name: str, logger: Optional[logging.Logger] = None):
        self.agent_name = agent_name
        self.logger = logger or setup_logging()

    def info(self, message: str) -> None:
        """Log info message"""
        full_message = f"[{self.agent_name}] {message}"
        self.logger.info(full_message)
        log_to_streamlit(full_message, "info")

    def success(self, message: str) -> None:
        """Log success message"""
        full_message = f"[{self.agent_name}] {message}"
        self.logger.info(full_message)
        log_to_streamlit(full_message, "success")

    def warning(self, message: str) -> None:
        """Log warning message"""
        full_message = f"[{self.agent_name}] {message}"
        self.logger.warning(full_message)
        log_to_streamlit(full_message, "warning")

    def error(self, message: str) -> None:
        """Log error message"""
        full_message = f"[{self.agent_name}] {message}"
        self.logger.error(full_message)
        log_to_streamlit(full_message, "error")
