# Langchain Demo with Gemma Model

This project is a simple AI-powered chatbot built using Streamlit and LangChain, utilizing the Gemma model from Ollama. It allows users to input a question and receive a response from the AI.

## Features
- Uses **LangChain** for structured AI interaction
- **Ollama** integration with the **Gemma 2B** model
- **Streamlit** for an interactive web-based interface
- Supports **environment variable configuration** using `dotenv`
- **Langsmith tracking** enabled for API calls

## Installation

### Prerequisites
- Python 3.8+
- Install dependencies using pip

```bash
pip install streamlit langchain langchain_community python-dotenv ollama
```

## Setup
1. Clone the repository:
```bash
git clone <repo-url>
cd <repo-name>
```
2. Create a `.env` file in the root directory and add the following environment variables:
```env
LANGCHAIN_API_KEY1=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
```
3. Run the application:
```bash
streamlit run app.py
```

## Code Overview
- **Prompt Template**: Defines the chat structure with system and user messages.
- **Ollama Model**: Uses the `gemma:2b` model for generating responses.
- **Streamlit UI**: Provides an interactive interface for users to input their questions.
- **Environment Variables**: Used for API keys and project tracking.

## Usage
- Run the Streamlit app.
- Enter a question in the input field.
- The AI will generate and display a response based on the `gemma:2b` model.



