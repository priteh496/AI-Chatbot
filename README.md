# 🤖 AI Chatbot using OpenAI API

## Description
A terminal-based AI chatbot powered by OpenAI GPT models. Supports multi-turn conversations with persistent history, configurable system prompts, and clean CLI interface.

## Features
- Multi-turn conversation with memory
- Configurable model, temperature, and max tokens
- View and clear conversation history
- Secure API key management via .env
- Error handling for API failures and rate limits

## Tech Stack
- Python 3.10+
- openai — GPT API client
- python-dotenv — Environment variable management

## Installation
```bash
cd project_1_ai_chatbot
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## How to Run
```bash
python main.py
```

## Example Output
```
You: What is the capital of France?
Assistant: The capital of France is Paris.

You: history
[12:01:00] User: What is the capital of France?
[12:01:01] Assistant: The capital of France is Paris.
```
