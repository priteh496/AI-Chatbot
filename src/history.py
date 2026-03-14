"""
Manages conversation history for the chatbot.
Stores messages and provides display utilities.
"""

from datetime import datetime
from typing import List, Dict


class ConversationHistory:
    """Stores and manages chat conversation history."""

    def __init__(self, max_messages: int = 20):
        """
        Initialize conversation history.

        Args:
            max_messages: Maximum number of messages to keep in memory
        """
        self.messages: List[Dict[str, str]] = []
        self.max_messages = max_messages
        self.timestamps: List[str] = []

    def add(self, role: str, content: str):
        """
        Add a message to history.

        Args:
            role: 'user' or 'assistant'
            content: Message content
        """
        self.messages.append({"role": role, "content": content})
        self.timestamps.append(datetime.now().strftime("%H:%M:%S"))

        # Trim history if too long (keep context window manageable)
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
            self.timestamps = self.timestamps[-self.max_messages:]

    def get_messages(self) -> List[Dict[str, str]]:
        """Return messages list for API consumption."""
        return self.messages.copy()

    def clear(self):
        """Clear all conversation history."""
        self.messages = []
        self.timestamps = []

    def display(self):
        """Print formatted conversation history."""
        if not self.messages:
            print("📭 No conversation history yet.")
            return

        print("\n" + "=" * 60)
        print("          CONVERSATION HISTORY")
        print("=" * 60)
        for i, (msg, ts) in enumerate(zip(self.messages, self.timestamps)):
            role_icon = "👤" if msg["role"] == "user" else "🤖"
            role_label = msg["role"].capitalize()
            print(f"[{ts}] {role_icon} {role_label}: {msg['content'][:100]}...")
        print("=" * 60)

    def __len__(self) -> int:
        return len(self.messages)
