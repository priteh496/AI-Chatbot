"""
AI Chatbot using OpenAI API
Entry point for the chatbot application.
"""

import sys
from src.chatbot import ChatBot
from src.history import ConversationHistory
from config import Config


def main():
    """Main function to run the AI chatbot."""
    print("=" * 60)
    print("        🤖  AI Chatbot powered by OpenAI GPT")
    print("=" * 60)
    print("Type 'quit' or 'exit' to stop.")
    print("Type 'history' to view conversation history.")
    print("Type 'clear' to clear conversation history.")
    print("-" * 60)

    # Initialize components
    config = Config()
    history = ConversationHistory()
    bot = ChatBot(api_key=config.OPENAI_API_KEY, model=config.MODEL, history=history)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye! 👋")
                sys.exit(0)

            if user_input.lower() == "history":
                history.display()
                continue

            if user_input.lower() == "clear":
                history.clear()
                print("✅ Conversation history cleared.")
                continue

            # Get response from chatbot
            response = bot.chat(user_input)
            print(f"\nAssistant: {response}")

        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
