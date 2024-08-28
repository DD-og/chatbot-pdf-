# PDF Chat Application

This application allows users to chat with multiple PDF documents using Streamlit and the Gemini language model.

## Features

- Upload multiple PDF documents
- Extract text from PDFs
- Process and chunk text for efficient retrieval
- Create a vector store for semantic search
- Chat interface to ask questions about the uploaded documents
- Utilizes the Gemini language model for generating responses

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Langchain
- HuggingFace Embeddings
- FAISS Vector Store
- Google's Generative AI (Gemini)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/pdf-chat-app.git
   cd pdf-chat-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the sidebar to upload your PDF documents and click "Process PDFs".

4. Once the PDFs are processed, you can start asking questions about the documents in the main chat interface.

## How It Works

1. The app allows users to upload multiple PDF files.
2. Text is extracted from the PDFs and split into manageable chunks.
3. The text chunks are embedded and stored in a FAISS vector store for efficient retrieval.
4. A custom Gemini LLM class is used to integrate with Google's Generative AI.
5. The app uses a ConversationalRetrievalChain to maintain context and generate relevant responses.
6. Users can interact with the documents through a chat interface, asking questions and receiving answers based on the content of the uploaded PDFs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
