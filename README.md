# PDF Query with Google Generative AI 📕🖨️
This project demonstrates a PDF-based Question-Answering System powered by Retrieval-Augmented Generation (RAG). The application allows users to upload a PDF document, ask questions about its content, and receive relevant answers through similarity search and AI embeddings.


# Project Overview 📄
The main goal of this project is to create a seamless interface where users can interact with the content of a PDF using natural language queries. We utilize Google Generative AI for generating embeddings and FAISS (Facebook AI Similarity Search) for efficient similarity-based retrieval.

This system is built using Streamlit, making it user-friendly and interactive. Users upload a PDF, and the system extracts its content, processes it into manageable chunks, and builds a searchable vector store to handle queries effectively.

![Image](https://github.com/user-attachments/assets/125cfd74-ddba-4961-9f19-257613a3e471)

# What is Retrieval-Augmented Generation (RAG)? 🤖

RAG is a hybrid machine learning approach that combines:

1. Information Retrieval: Searching for relevant information from a large dataset or documents.

2. Generation: Using a language model to generate a natural language response based on the retrieved information.


![Image](https://github.com/user-attachments/assets/0314db0b-8db2-41d1-aed4-487667b6ab25)

# Benefits of RAG:

• Enhanced Contextual Understanding: Provides more accurate answers by leveraging retrieved relevant context.

• Improved Efficiency: Retrieves only the necessary chunks of information, reducing computational overhead.

• Dynamic Updates: Easily incorporates new or updated data without retraining the model.

• Better Accuracy: Works well even with small models as it fetches high-quality, relevant context before generating responses.



# Steps in the Project Workflow 🛠️

1.Upload PDF:

• The user uploads a PDF document via the Streamlit interface.

2.Text Extraction:

• The PDF content is extracted using PyPDFLoader.

3.Text Splitting:

• The extracted content is split into smaller chunks using RecursiveCharacterTextSplitter. This helps in creating meaningful embeddings and managing large documents.

4.Embedding Creation:

• Each text chunk is embedded into a high-dimensional space using Google Generative AI embeddings.

5.Vector Store Initialization:

• The embeddings are stored in a FAISS vector store, enabling fast similarity-based searches.

6.Query Input:

• Users enter their query into the interface.

7.Similarity Search:

The system searches the vector store for the most relevant chunks based on the user's query.

8.Display Results:

The top result is displayed as the answer to the user's query.


# Features 🚀

• Upload PDF: Supports easy document uploads.

• Interactive Interface: User-friendly question input and response display.

• Efficient Search: Uses similarity search to find relevant information quickly.

• Accurate Results: Leverages Google Generative AI embeddings for high-quality text representations.


# Why Similarity Search? 🔍

Similarity search is a key part of the RAG framework. It allows the system to compare the user's query with precomputed document embeddings, finding the most relevant text chunks. This ensures that the system provides accurate and contextually relevant answers, even when dealing with large or complex documents.


# Technologies Used 💻

• Streamlit: For building an interactive web application.

• Google Generative AI: For generating text embeddings.

• FAISS: For fast similarity-based searches.

• LangChain: For managing document loaders, text splitters, and embeddings.




# Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/Simple_PDF_RAG/blob/main/Demo.gif)
