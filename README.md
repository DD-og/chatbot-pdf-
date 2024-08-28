# Chat with Multiple PDFs


## Flowchart
![flowchart](https://github.com/user-attachments/assets/9582ed37-69d5-4a28-b163-e369b4538177)


## Overview

This Streamlit app allows users to upload multiple PDF documents, extract their text, and interact with the content using a conversational AI model. The app leverages the Gemini model from Google Generative AI and integrates it with a vector store for document retrieval and chat-based interactions.

## Features

* Upload and process multiple PDF files.
* Extract text from PDFs and split it into manageable chunks.
* Create a vector store using HuggingFace embeddings for efficient text retrieval.
* Engage in a conversation with the processed documents using the Gemini LLM model.
* Customizable chat interface with user and bot templates.

## Prerequisites

1. Python 3.7+
2. Streamlit
3. Google Generative AI API key
4. Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/DD-og/chatbot-pdf-.git>
   cd <charbot-pdf>
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory of the project and add your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the sidebar to upload your PDF documents and click "Process PDFs".

4. Once the PDFs are processed, you can start asking questions about the documents in the main chat interface.

## How It Works

1. The app allows users to upload multiple PDF files.
2. Text is extracted from the PDFs using PyPDF2 and split into manageable chunks.
3. The text chunks are embedded using HuggingFace Embeddings and stored in a FAISS vector store for efficient retrieval.
4. A custom GeminiLLM class is used to integrate with Google's Generative AI.
5. The app uses a ConversationalRetrievalChain to maintain context and generate relevant responses.
6. Users can interact with the documents through a chat interface, asking questions and receiving answers based on the content of the uploaded PDFs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
