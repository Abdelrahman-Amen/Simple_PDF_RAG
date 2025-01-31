# Import required libraries
import streamlit as st  # For creating the web application interface
import os  # For accessing environment variables and file paths
from dotenv import load_dotenv  # To load environment variables from a .env file
from langchain_community.document_loaders import PyPDFLoader  # To load and process PDF documents
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text into manageable chunks
from langchain_community.vectorstores import FAISS  # For creating and managing a vector store
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # For embeddings using Google Generative AI
import google.generativeai as genai  # Google Generative AI client library

# Load environment variables from a .env file
load_dotenv()

# Configure the Google Generative AI API with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the main function for the Streamlit app
def main():
    # Set the title of the web application
    st.title("PDF Query with Google Generative AI")

    # Allow the user to upload a PDF file through a file uploader
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Save the uploaded file to the local directory as "uploaded_file.pdf"
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display a success message
        st.success("PDF uploaded successfully!")

        # Load the uploaded PDF file using PyPDFLoader
        loader = PyPDFLoader("uploaded_file.pdf")
        docs = loader.load()  # Extract the text content of the PDF

        # Split the text content into smaller chunks for processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
        documents = text_splitter.split_documents(docs)

        # Initialize a FAISS vector store with the document chunks and Google Generative AI embeddings
        db = FAISS.from_documents(documents, GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

        # Create a text input field for the user to enter their query
        query = st.text_input("Enter your query")

        # When the "Search" button is clicked and a query is provided
        if st.button("Search") and query:
            try:
                # Perform a similarity search in the vector store using the user's query
                result = db.similarity_search(query)

                # Display the top search result if found
                if result:
                    st.subheader("Top Result:")
                    st.write(result[0].page_content)
                else:
                    # Display a warning if no results are found
                    st.warning("No results found.")
            except Exception as e:
                # Handle any errors that occur during processing
                st.error(f"An error occurred: {e}")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
