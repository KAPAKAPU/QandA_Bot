# QandA_Bot
QandA_Bot: Document-Based Question Answering Bot

This project is an interactive Question Answering (QA) bot that allows users to upload PDF documents and ask questions based on the content of the uploaded files. It uses machine learning models like Cohere for natural language processing and Pinecone for efficient document indexing and querying.

Features

	•	PDF Upload and Processing: Users can upload documents in PDF format, which are then processed to extract text.
	•	Real-Time Q&A: Users can ask questions related to the content of the uploaded document and receive real-time answers.
	•	Document Retrieval: The bot retrieves relevant document segments based on the user’s query, providing contextually accurate responses.
	•	Streamlit Frontend: An intuitive interface built using Streamlit for seamless user interaction.
	•	Scalable and Efficient: Designed to handle large documents and multiple queries without performance drops.


QandA_Bot/
│
├── .streamlit/                    # Streamlit specific configurations
│   └── secrets.toml               # Contains API keys and secrets
│
├── documents/                     # Directory for uploaded documents (optional, if needed for storage)
│
├── app.py                         # Main Streamlit application file (frontend)
│
├── backend.py                     # Backend logic for embedding and querying with Cohere and Pinecone
│
├── pdf_processing.py              # PDF processing and text extraction logic
│
├── requirements.txt               # List of required Python packages for the project
│
└── Dockerfile                     # Docker configuration file for containerizing the application
