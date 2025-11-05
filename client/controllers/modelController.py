from services.modelService import ModelService
from validations.chatData import ChatData,ChatMessage
from services.chatBotService import ChatBotService 
from fastapi.responses import JSONResponse  
from rich import print

class ModelController:
     def __init__(self):
          self.collectionChat = ModelService()
          model_service = ChatBotService()
     
     def create_new_chat(self, chat_data: ChatData):
           try:
               self.collectionChat.save_chat(chat_data,)
               response = ChatBotService().generate_response(chat_data.messages)
               ai_message = ChatMessage(types="ai", message=str(response.content))

               self.collectionChat.save_chat(
                   ChatData(
                       id_session=chat_data.id_session,
                       user_id=chat_data.user_id,
                       messages=[ai_message]
                   )
               )

               return JSONResponse(content={"response": response.content}, status_code=200)
           except Exception as e:
               print(f"[red]Error in create_new_chat: {e}[/red]")
               return JSONResponse(content={"error": "Failed to create chat"}, status_code=500)     
            
     def get_chat_by_id(self, chat_id):
          return self.collectionChat.getChatById(chat_id)
     
     def get_all_chats(self):
          return self.collectionChat.getAllChats()