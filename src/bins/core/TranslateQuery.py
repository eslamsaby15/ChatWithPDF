from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from .BaseState import Basestate

def TranslateQuery(state :Basestate):
    "Machine Translation to translate Queries to english text"

    llm = Basestate.llm
    user_messages = [m for m in state["messages"] if isinstance(m,HumanMessage)]
    question = state.get("translated_query", user_messages[-1].content)
    

    msg_prompt = f"""
                    You are a Machine Translation (MT) system.
                    Your task: translate the user question to English text.

                    Instructions:
                    1. Translate the question to English as accurately as possible.
                    2. Do not add explanations, comments, or extra content.
                    3. Do not attempt to clarify or modify the meaning.
                    4. Keep the original meaning exactly.

                    User question: "{question}"
                    """

    prompt_msg_template = PromptTemplate(
        template=msg_prompt,
        input_variables=['question']
    )

    resonong = llm.invoke([{'role': 'user', 'content': prompt_msg_template.format(question=question)}])

    return {'messages': [HumanMessage(content=resonong.content)]}
