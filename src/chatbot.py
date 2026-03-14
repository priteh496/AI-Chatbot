"""
Core chatbot logic using OpenAI API.
Handles message sending and response parsing.
"""

import openai
from src.history import ConversationHistory


class ChatBot:
    """Handles communication with OpenAI Chat Completions API."""

    def __init__(self, api_key: str, model: str, history: ConversationHistory):
        """
        Initialize the chatbot.

        Args:
            api_key: OpenAI API key
            model: Model name (e.g., gpt-3.5-turbo)
            history: ConversationHistory instance
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.history = history
        self.system_prompt = (
            "You are a helpful, friendly, and knowledgeable AI assistant. "
            "Answer questions clearly and concisely."
        )

    def chat(self, user_message: str) -> str:
        """
        Send a message and get a response.

        Args:
            user_message: The user's input message

        Returns:
            Assistant's response as a string
        """
        # Add user message to history
        self.history.add("user", user_message)

        # Build messages list with system prompt + history
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.history.get_messages())

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7,
            )
            assistant_reply = response.choices[0].message.content.strip()

            # Save assistant reply to history
            self.history.add("assistant", assistant_reply)
            return assistant_reply

        except openai.AuthenticationError:
            raise Exception("Invalid OpenAI API key. Please check your .env file.")
        except openai.RateLimitError:
            raise Exception("Rate limit exceeded. Please wait and try again.")
        except openai.APIConnectionError:
            raise Exception("Could not connect to OpenAI API. Check your internet.")
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
