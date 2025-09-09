from .ProcessingDocuments import (get_content_pages , 
                                 split_chunks ,
                                 create_vectorDB)

from langchain.tools.retriever import create_retriever_tool 
from langgraph.prebuilt import create_react_agent
from .BaseState import Basestate

# Create VectorDB
def VectorDB(files:list[str]) :
    """concat all together""" 
    
    content = get_content_pages(files=files)
    chunks = split_chunks(content)
    vectorDB = create_vectorDB(chunks)
    return vectorDB 



# retieve Tool
def create_retrivertool(vector_db  ):

    retriver = vector_db.as_retriever()
    retrivertool = create_retriever_tool(retriver , 
                                     "retriever_tool" ,
                                     "Search and return information about input context" )

    return retrivertool


# retriever Agient
def create_RetriverAgent( retrivertool) : 
    llm = Basestate.llm
    RetriverAgent = create_react_agent(
        llm,
        tools=[retrivertool],
        name="RetriverAgent",
        prompt=(
            "You are a retriever agent.\n"
            "- Otherwise, always call the retriever_tool with the user query.\n"
            "- Return ONLY the page_content of the retrieved documents.\n"
            "- Do not summarize or rephrase.\n"
            "- Don't return repeated retrieved chunks.\n"
            "- If you didn't find similar text return 'I can't find it'."
        )
    )

    return RetriverAgent