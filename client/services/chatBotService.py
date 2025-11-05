from config.llm import geminiModel
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class ChatBotService:
     def __init__(self):
          self.model = geminiModel
     
     def generate_response(self, messages):
          response = self.model.invoke([
                SystemMessage(content="Eres un asistente de competencia de productos."),
                HumanMessage(content="Analiza el iPhone Pro Max en Argentina.")
            ])
          return response
