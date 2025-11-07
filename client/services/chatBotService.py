from config.llm import getModel
from helpers.extractResponse import extraer_respuesta_aimessage
from rich import print


class ChatBotService:
     def __init__(self):
         self.model = None
 
     async def load_model(self):
        self.model = await getModel()
        if self.model is None:
           raise RuntimeError("El modelo no se pudo cargar. getModel() devolvió None.")

     async def generate_response(self, message: str):
        if self.model is None:
                 return RuntimeError("No se puede generar respuesta: el modelo no está cargado.")
     
        response = await self.model.ainvoke({
              "messages": [{"role": "user", "content": message}]
          })
        
        print(response)
        print(extraer_respuesta_aimessage(response["messages"][-1]))
        
        return extraer_respuesta_aimessage(response["messages"][-1])
