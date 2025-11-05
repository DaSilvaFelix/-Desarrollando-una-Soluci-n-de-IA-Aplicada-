from langchain_google_genai import ChatGoogleGenerativeAI
from config.env import EnvConfig
from pydantic import SecretStr

env = EnvConfig()
gemini_api_key = env.get("GEMINI_API_KEY")

geminiModel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=SecretStr(gemini_api_key) if gemini_api_key is not None else None
)