from .BaseState import Basestate
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import  AIMessage
def TranslationReasoning(state: Basestate):
    
    """Translate the reasoning into the same **language** and **dialect** of the question."""
    
    llm = Basestate.llm
    context = state["messages"][-1].content
    detected_lang = state.get("detected_lang")
    dialect = state.get("dialect")


    Translatetemplate = "\n".join([
        "You are a translation agent. Your ONLY job is to translate English text into the target language below.",
        "Never answer in Spanish, French, or any other language unless it exactly matches the detected language.",
        "you must know we shortcut the two-character ISO 639-1 code for the language like ar for arabic , en for english ",
        "",
        f"Target language: {detected_lang} ",
        f"Target dialect: {dialect or 'standard'}",
        "",
        "# Instructions:",
        "- If dialect is None, translate to the language only.",
        "- If the language is not English, keep important keywords in English.",
        "- Don't explain, don't rephrase, just translate.",
        "- If target language is Arabic, mimic the dialect if possible; otherwise use Modern Standard Arabic.",
        "",
        "Text to translate to targey language : ",
        "{context}"
    ])

    TranslatePrompt = PromptTemplate(
        template=Translatetemplate,
        input_variables=["context"],
    )

    prompt = TranslatePrompt.format(context=context)

    response = llm.invoke([
        {"role": "system", "content": "You are a strict translation agent. Respond ONLY with the translated text."},
        {"role": "user", "content": prompt}
    ])
    
    
    translated_text = response.content 
    return {"messages": [AIMessage(content=translated_text)]}