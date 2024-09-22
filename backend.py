import cohere
import pinecone
import streamlit as st

# Load secrets
cohere_api_key = st.secrets["COHERE_API_KEY"]
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
pinecone_environment = st.secrets["PINECONE_ENVIRONMENT"]

# Initialize Cohere and Pinecone
co = cohere.Client(cohere_api_key)
pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)
index = pinecone.Index("your-index-name")

def query_backend(query):
    # Generate embedding for the query
    response = co.embed(texts=[query])
    query_embedding = response.embeddings[0]
    
    # Query Pinecone for similar documents
    response = index.query(vector=query_embedding, top_k=3, include_values=False, include_metadata=True)
    
    # Retrieve document segments
    retrieved_texts = [match['metadata'].get('content', 'No content available') for match in response['matches']]
    
    # Combine retrieved segments and return as answer
    context = "\n".join(retrieved_texts)
    return context

# Note: Ensure to handle errors and validate responses appropriately in production.