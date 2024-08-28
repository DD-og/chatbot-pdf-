import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms.base import LLM
from typing import Any, List, Optional
import google.generativeai as genai
import os
from htmlTemplates import css, bot_template, user_template

# Custom LLM class for Gemini
class GeminiLLM(LLM):
    model: Any
    
    def __init__(self, model):
        super().__init__()
        self.model = model

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    @property
    def _identifying_params(self):
        return {"model": self.model}

    @property
    def _llm_type(self):
        return "Gemini"

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create vector store
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create conversation chain
def get_conversation_chain(vectorstore):
    # Initialize Gemini
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=GeminiLLM(model),
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input
def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    if "chat_history" in st.session_state:
        st.markdown(css, unsafe_allow_html=True)  # Add CSS
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.markdown(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Main function
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":books:")

    st.sidebar.header("Upload and Process PDFs")
    pdf_docs = st.sidebar.file_uploader(
        "Upload your PDFs here (multiple files allowed)", accept_multiple_files=True)
    process_button = st.sidebar.button("Process PDFs")

    if process_button:
        if pdf_docs:
            with st.spinner("Processing your PDFs..."):
                try:
                    # Extract and process PDF text
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.success("PDFs processed successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload PDF files to process.")

    st.header("Chat with Your Documents")
    user_question = st.text_input("Ask a question about your documents:")
    
    if user_question:
        if st.session_state.conversation:
            handle_userinput(user_question)
        else:
            st.warning("Please process your PDFs first.")

if __name__ == '__main__':
    main()
