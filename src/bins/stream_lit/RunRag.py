from streamlit_chat import message
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

def Chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input("Your message:")
    if 'graph' in st.session_state and prompt:
            st.session_state.messages.append(HumanMessage(content=prompt))

            state_input = {
                "messages": st.session_state.messages
            }

            resoning = st.session_state.graph.invoke(
                state_input,
                config={"configurable": {"thread_id": "1"}}
            )
            
            st.session_state.messages.append(
                AIMessage(content=resoning['messages'][-1].content)
            )

            for i, msg in enumerate(st.session_state.messages):
                if isinstance(msg, HumanMessage):
                    message(msg.content, is_user=True, key=str(i) + '_user')
                elif isinstance(msg, AIMessage):
                    message(msg.content, is_user=False, key=str(i) + '_ai')


    