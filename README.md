# ChatWith-Multi-PDFS / Docs

A simple **Chat with Multiple PDFs / Docs** app for **Retrieval-Augmented Generation (RAG)**.  
It allows you to ask questions about the contents of PDFs and DOC files, and the app AI-powered answers based on relevant responses.

![Chatbot Diagram](/src/images/GraghWorkFlow.jpg)

This app is built using [**LangGraph**](https://www.langchain.com/langgraph) and [**LangChain**](https://www.langchain.com/).



------
## 🚀 Features covered

- **Multi-Document Support**: Reads and processes both PDF and DOC files.  
- **Text Chunking**: Splits extracted text into manageable overlapping chunks.  
- **Semantic Embeddings**: Generates vector embeddings using state-of-the-art models.  
- **Vector Database**: Stores embeddings in a scalable vector DB for fast similarity search.  
- **Detection of Language and Dialect**: Automatically detects language and Arabic dialects if applicable.  
- **Retriever Tool**: Fetches the most relevant chunks using semantic search.  
- **Graders**: Evaluate the relevance of retrieved documents before generating answers.  
- **Translate & Reasoning**: Provides translation support and reasoning over queries.  
- **Query Handling**: Processes user queries for context-aware responses.  
- **LLM-Powered Answering**: Combines retrieved context with queries to generate factual, context-aware answers.  
- **Streamlit Integration**: Fully interactive interface for uploading documents and chatting with the AI assistant.
-----
## 🔹 Workflow

### 1. Language & Dialect Detection 🌐
- Detect the language of the user query.
- Detect dialects if the query is in Arabic or other supported languages.
- Translate the query to English for processing.

### 2. Database Preparation 🗂️
- Extract text from PDF/DOC files.
- Split text into smaller overlapping chunks.
- Generate embeddings and store them in the vector database.

### 3. Retrieval & Grading 🔎⚙️
- Use the retriever tool to fetch relevant chunks based on the translated query.
- Graders evaluate the relevance of the retrieved chunks.
- Decide workflow:
  - **Generate Answer** → if relevant chunks are found.
  - **Chitchat / fallback** → if no relevant context is retrieved.

### 4. Answer Generation ✨
- Combine retrieved context (if any) with the translated query.
- Pass to the LLM → produce answer in English.

### 5. Output Translation & Presentation 🌍
- Translate the generated answer back to the original language and dialect of the query.
- Display the answer in Streamlit with proper formatting.

-----


# 📂 ChatWithPDF - Structure

```bash
src/
│   app.py
│   requirements.txt
│   workflow.ipynb
│
├───bins
│   ├───core
│   │   ├── BaseState.py
│   │   ├── Chit_Chat.py
│   │   ├── Dectionlang.py
│   │   ├── Generation.py
│   │   ├── Grade.py
│   │   ├── ProcessingDocuments.py
│   │   ├── Retrieve.py
│   │   ├── TranslateQuery.py
│   │   └── TranslateReasoning.py
│   │
│   ├───stream_lit
│   │   ├── loadingFiles.py
│   │   ├── RunRag.py
│   │   └── SetUP.py
│   │
│   └───WorkFlow
│       └── Graph.py
│
├───data/      
│
└───images/   

```
-----

## 📦 Installation

### Requirements
- Python 3.11  

###  Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)  

2) Create a new environment:
```bash
conda create -n chat python=3.11
```

3) Activate the environment:
```bash
$ conda activate chat
```

4) Install the required packages
```bash
$ pip install -r requirements.txt
```

5) Setup the environment variables

```bash
$ cp .env.example .env
```

6) Run streamlit app
```bash
$ streamlit run app.py
```
-----------


![Chatbot ](/src/images/example.jpg)

---------
## 🔹 Conclusion  

- Demonstrates how **Chat with Multiple PDFs / Docs** pipeline can be built using **RAG (Retrieval-Augmented Generation)**.  

- Steps:  

  1. **Language & Dialect Detection** → detect the user query language and dialect, translate to English for processing.  

  2. **Database Preparation** → extract text from PDF/DOC files, split text into overlapping chunks, create embeddings, and store them in the vector database.  

  3. **Retrieval & Grading** → fetch relevant chunks using the retriever tool, grade their relevance, and decide workflow:
     - **Generate Answer** → if relevant chunks are found.
     - **Chitchat / fallback** → if no relevant context is retrieved.  

  4. **Answer Generation** → combine retrieved context with the translated query, generate the answer via LLM.  

  5. **Output Translation & Presentation** → translate the generated answer back to the original language and dialect, display it in Streamlit with proper formatting.  
---------

## 👨‍💻 Built by Eslam Sabry

concat
🔗 [LinkedIn](https://www.linkedin.com/in/eslamsabryai)   🔗 [Kaggle](https://www.kaggle.com/eslamsabryelsisi)  

