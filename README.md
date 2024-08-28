Chat with Multiple PDFs

Overview

This Streamlit app allows users to upload multiple PDF documents, extract their text, and interact with the content using a conversational AI model. The app leverages the Gemini model from Google Generative AI and integrates it with a vector store for document retrieval and chat-based interactions.

Features

Upload and process multiple PDF files.
Extract text from PDFs and split it into manageable chunks.
Create a vector store using HuggingFace embeddings for efficient text retrieval.
Engage in a conversation with the processed documents using the Gemini LLM model.
Customizable chat interface with user and bot templates.
Prerequisites

Python 3.7+
Streamlit
Google Generative AI API key
Required Python libraries (listed in requirements.txt)
Installation

Clone the repository:
bash
Copy code
git clone <repository-url>
cd <repository-directory>
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory of the project and add your Gemini API key:

makefile
Copy code
GEMINI_API_KEY=your_api_key_here
Usage

Run the Streamlit app:
bash
Copy code
streamlit run app.py
Upload PDFs:
Open the app in your browser.
Use the sidebar to upload multiple PDF files.
Click "Process PDFs" to extract and process the text.
Ask Questions:
After processing the PDFs, type your questions in the input field to interact with the documents.
The app will display responses from the AI model, formatted using custom HTML templates.
Code Explanation

GeminiLLM Class: Custom class to integrate the Gemini model with Langchain’s LLM interface.
get_pdf_text Function: Extracts text from uploaded PDF files.
get_text_chunks Function: Splits the extracted text into chunks for efficient processing.
get_vectorstore Function: Creates a vector store from the text chunks using HuggingFace embeddings.
get_conversation_chain Function: Sets up the conversation chain with the Gemini LLM model and vector store.
handle_userinput Function: Handles user input and displays chat history with custom HTML/CSS styling.
HTML/CSS Templates

CSS: Defines the styles for the chat interface, including user and bot message styling.
bot_template: HTML template for displaying bot messages.
user_template: HTML template for displaying user messages.
Troubleshooting

Ensure you have a valid Gemini API key and it is correctly set in the .env file.
Verify all required Python libraries are installed.
