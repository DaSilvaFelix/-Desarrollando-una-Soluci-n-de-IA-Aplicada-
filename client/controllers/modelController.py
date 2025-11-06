from services.modelService import ModelService
from validations.chatData import ChatData, ChatMessage
from services.chatBotService import ChatBotService
from fastapi.responses import JSONResponse
from rich import print


model_service = ChatBotService()


class ModelController:
    def __init__(self):
        self.collectionChat = ModelService()
        self.model_service = ChatBotService()

    async def create_new_chat(self, chat_data: ChatData):
        try:
            self.collectionChat.save_chat(chat_data)

            await self.model_service.load_model()
            response = await self.model_service.generate_response(chat_data.messages[-1].message)
            
            ai_message = ChatMessage(types="ai", message=response)

            self.collectionChat.save_chat(
                ChatData(
                    id_session=chat_data.id_session,
                    user_id=chat_data.user_id,
                    messages=[ai_message]
                )
            )

            return JSONResponse(content={"response": response}, status_code=200)
        except Exception as e:
            print(f"[red]Error in create_new_chat: {e}[/red]")
            return JSONResponse(content={"error": "Failed to create chat"}, status_code=500)

    def get_chat_by_id(self, chat_id):
        return self.collectionChat.getChatById(chat_id)

    def get_all_chats(self):
        return self.collectionChat.getAllChats()
