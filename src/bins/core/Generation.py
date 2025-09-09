from .BaseState import Basestate
from langchain_core.messages import HumanMessage

def GenerateAnswer(state: Basestate) :
    """Generate an answer."""

    GENERATE_PROMPT = "\n".join([
        "You are an assistant for question-answering tasks.",
        "Use the following pieces of retrieved context to answer the question.",
        "- you must first understand the question and the context to answer correctly.",
        "Answer as many questions as possible and make it a simple temporary one.",
        "- Generate english text only.",
        "- If the question is a greeting or introductory (like 'how are you', 'what's up', 'hello', 'hi', or self-introduction like 'I am X'), do not use the context. Instead, just greet back politely and say 'How can I help you?'.",
        "- If it is a normal question, add some information from the context in your answer to make it complete, not only from the context.",
        "Question: {question}\n",
        "Context: {context}"
    ])
    llm = Basestate.llm

    user_messages = [m for m in state["messages"] if isinstance(m,HumanMessage)]
    
    question = state.get("translated_query", user_messages[-1].content)
    context = state["messages"][-1].content

    prompt = GENERATE_PROMPT.format(question=question, context=context)
    response = llm.invoke([{"role": "user", 
                            "content": prompt}])
    
    return {"messages": [response]}