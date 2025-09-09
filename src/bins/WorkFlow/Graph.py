from langgraph.graph import START, END, StateGraph
from bins.core import Basestate
from bins.core import  create_RetriverAgent  ,create_retrivertool ,VectorDB
from bins.core import detecting_language , TranslateQuery , chitChatAgent ,GenerateAnswer ,TranslationReasoning ,GraderDocumentAgent



class WorkFlow :
    
    def __init__(self, pdfs: list[str]): 
        self.workflow = StateGraph(Basestate)
        self.vectorDB = VectorDB(pdfs)
        self.retrieve_tool = create_retrivertool(self.vectorDB)
        self.RetriverAgent = create_RetriverAgent( retrivertool=self.retrieve_tool)
  
    def create_Graph(self):
        self.workflow.add_node("DetectLangAgent", detecting_language)
        self.workflow.add_node("Translate_Query", TranslateQuery)
        self.workflow.add_node("RetriverAgent", self.RetriverAgent)
        self.workflow.add_node("Chit-ChatAgent", chitChatAgent)
        self.workflow.add_node("AnswerAgent", GenerateAnswer)
        self.workflow.add_node("TranslationReasoning", TranslationReasoning)

        self.workflow.add_edge(START, "DetectLangAgent")
        self.workflow.add_edge("DetectLangAgent", "Translate_Query")
        self.workflow.add_edge("Translate_Query", "RetriverAgent")

        self.workflow.add_conditional_edges(
            "RetriverAgent",
            GraderDocumentAgent,
            {
                "AnswerAgent": "AnswerAgent",
                "Chit-ChatAgent": "Chit-ChatAgent",
            }
        )

        self.workflow.add_edge("AnswerAgent", "TranslationReasoning")
        self.workflow.add_edge("Chit-ChatAgent", "TranslationReasoning")
        self.workflow.add_edge("TranslationReasoning", END)

        return self.workflow.compile()

