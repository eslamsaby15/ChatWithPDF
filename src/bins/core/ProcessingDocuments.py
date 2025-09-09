from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore


# 1. Reading Files
def get_content_pages(files:  list[str]) -> str:
    """Read PDF or TXT files and return their combined text"""
    ftext = ""
    for file_path in files:
        if file_path.lower().endswith(".pdf"):
            pdf_loader = PdfReader(file_path)
            for page in pdf_loader.pages:
                ftext += page.extract_text() or ""  
        else:
            with open(file_path, "r", encoding="utf-8") as f:
                ftext += f.read()
        ftext += "\n"
    return ftext


# 2. Split to Chunks
def split_chunks(text : str , chunk_size :int = 450, chunk_overlap : int = 50) :
    """Split to small and overla chunks"""
    splitter= RecursiveCharacterTextSplitter("\n", chunk_size =chunk_size , 
                                         chunk_overlap =chunk_overlap)
    chunks = splitter.split_text(text)

    return chunks



# 3. Create vector DB
def create_vectorDB(chunks : list[str] ,
                    embedding_name  : str = "sentence-transformers/all-MiniLM-L6-v2" ) : 
    """Generate and store embedding of chunks into vector database"""
    embedding_model = HuggingFaceEmbeddings(model_name = embedding_name)
    vectordb = InMemoryVectorStore.from_texts(chunks , embedding_model)
    return vectordb