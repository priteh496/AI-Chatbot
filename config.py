"""
Configuration for AI Chatbot.
Loads environment variables from .env file.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment."""

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MODEL: str = os.getenv("MODEL", "gpt-3.5-turbo")
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "500"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    SYSTEM_PROMPT: str = os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful, friendly, and knowledgeable AI assistant. "
        "Answer questions clearly and concisely."
    )

    def validate(self):
        """Validate required configuration values."""
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set. Check your .env file.")
