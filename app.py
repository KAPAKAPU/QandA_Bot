import streamlit as st
from backend import query_backend
import pdf_processing

def main():
    st.title("Interactive Q&A Bot")

    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
    if uploaded_file is not None:
        # Process the PDF and extract text
        text = pdf_processing.extract_text_from_pdf(uploaded_file)
        st.write("Document text extracted successfully.")
        
        # Send document text to the backend for embedding
        # Assuming `text` is being processed and stored in Pinecone in backend.py
        st.write("Text is being processed...")

    # Input query from the user
    query = st.text_input("Ask a question about the document:")
    if query:
        response = query_backend(query)
        st.write("Answer:", response)

if __name__ == "__main__":
    main()