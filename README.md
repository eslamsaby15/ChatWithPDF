# ChatWith-Multi-PDF

A simple **Chat with Multiple PDFs / Docs** app for **Retrieval-Augmented Generation (RAG)**.  
It allows you to ask questions about the contents of PDFs and DOC files, and the app AI-powered answers based on relevant responses.

![Chatbot Diagram](/src/images/graphWorkFlow.jpg)









------------

## 📦 Installation

### Requirements
- Python 3.11  

###  Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)  

2) Create a new environment:
```bash
conda create -n Chat python=3.11
```

3) Activate the environment:
```bash
$ conda activate Chat
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
---