from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage , HumanMessage
from .BaseState import Basestate

def chitChatAgent(state : Basestate):
    user_messages= [m for m in state['messages'] if isinstance(m,HumanMessage)]
    question = state.get("translated_query", user_messages[-1].content)
    llm = Basestate.llm
    
    msg_prompt = f"""
        You are a Chit-Chat Assistant.
        Your task: reply politely when the context not related to  a user question so follow Instructions to senf a chit chat message.
        
        Instructions:
        1. Start by apologizing that you don't fully understand the question.
        2. Try to clarify by highlighting key words from the user's question.
        3. Use short, simple sentences to suggest that the user rephrase their question.
        5. shorts apologizing messages in first sentence only.
        6. write in english text only.
        7. don't require any language from user to write his question.
        8. ask only some question trying to understand user question
        

        User question: "{question}"
        """

    prompt_msg_template = PromptTemplate(
        template=msg_prompt,
        input_variables=['question']
    )

    resonong = llm.invoke([{'role': 'user', 'content': prompt_msg_template.format(question=question)}])

    return {'messages': [AIMessage(content=resonong.content)]}
