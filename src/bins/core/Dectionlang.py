from pydantic import Field, BaseModel
from langgraph.graph import MessagesState
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from .BaseState import Basestate



class LanguageDetector(BaseModel):
    language: str = Field(
        description="Detected language of the question, represented in a two-character ISO 639-1 code."
    )


dialect_model_name = "IbrahimAmin/marbertv2-arabic-written-dialect-classifier"

dialect_pipeline = pipeline(
    "text-classification",
    model=AutoModelForSequenceClassification.from_pretrained(dialect_model_name),
    tokenizer=AutoTokenizer.from_pretrained(dialect_model_name),
)


def detecting_language(state: Basestate):
    
    llm  = Basestate.llm
    user_messages = [m for m in state["messages"] if isinstance(m, HumanMessage)]
    question = state.get("translated_query", user_messages[-1].content)
    
    detectionmodel = llm.with_structured_output(LanguageDetector)

    LANGUAGE_DETECTOR_TEMPLATE = "\n\n".join([
        "You are a language detector assessing to return the language of the question from a user.",
        "Here is the user question: {question}",
        "# Instructions:",
        "- Return only the two-character ISO 639-1 code for the language.",
        "- Base detection on the language of the question itself (its structure and wording), not on individual foreign words inside it.",
        "- Focus especially on the interrogative word (e.g., what, how, من, ماذا) and the main verb or auxiliary verb."
    ])


    detection_prompt = PromptTemplate(
        template=LANGUAGE_DETECTOR_TEMPLATE,
        input_variables=["question"]
    )


    prompt = detection_prompt.format(question=question)
    response: LanguageDetector = detectionmodel.invoke(prompt)


    # dialect
    dialect = None
    if response.language == "ar":
        preds = dialect_pipeline(question, top_k=None)
        if preds:
            best = max(preds, key=lambda x: x["score"])
            dialect = best["label"]
    
    
    return {
        "messages": state["messages"],
        "detected_lang": response.language,
        "dialect": dialect
    }

