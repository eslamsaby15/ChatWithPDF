import os
import dotenv
from typing import TypedDict
from typing import List
from langchain_core.messages import BaseMessage
from langchain.chat_models.base import BaseChatModel
from langchain.chat_models import init_chat_model


os.environ['GOOGLE_API_KEY'] = dotenv.get_key(key_to_get='GOOGLE_API_KEY', dotenv_path='.env')

class Basestate(TypedDict):
    messages: List[BaseMessage] = []
    detected_lang: str = ""
    dialect: str = ""
    llm: BaseChatModel =  init_chat_model(model='gemini-2.5-flash', model_provider='google-genai')

