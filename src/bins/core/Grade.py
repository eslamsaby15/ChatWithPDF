from pydantic import BaseModel , Field
from typing import Literal
from langchain_core.messages import HumanMessage
from .BaseState import Basestate
from langchain_core.prompts import PromptTemplate

class GraderDocument(BaseModel):
    """Grade documents using a binary score for relevance check."""
    binary_score : str = Field(description= "Relevance score: 'yes' if relevant, or 'no' if not relevant")


def GraderDocumentAgent(state: Basestate)-> Literal['Chit-ChatAgent' ,'AnswerAgent'] :
    
    user_messages = [m for m in state["messages"] if isinstance(m, HumanMessage)]
    question = state.get("translated_query", user_messages[-1].content)
    context = state['messages'][-1].content
    llm = Basestate.llm
      
    gradermodel = llm.with_structured_output(GraderDocument)
    
    GRADE_PROMPT = "\n\n".join([
    "You are a grader assessing relevance of a retrieved document to a user question.",
    "Here is the retrieved document: \n\n {context}",
    "Here is the user question: {question}",
    "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.",
    "If the question is an introductory or personal question (e.g., greetings like 'how are you', or self-introduction like 'I am X'), always grade it as 'yes'.",
    "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question." ])
    
    prompt = PromptTemplate(template= GRADE_PROMPT , input_variables=['question', 'context'])
    
    
    prompt_template = prompt.format(question = question , context = context)
    response =  gradermodel.invoke(
        [HumanMessage(content=prompt_template) ]
    )

    score = response.binary_score
    
    if score == 'yes' :
        return "AnswerAgent"
    else : 
        return 'Chit-ChatAgent'
    


