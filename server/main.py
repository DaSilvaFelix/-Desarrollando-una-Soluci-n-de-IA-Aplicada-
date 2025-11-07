from mcp.server import FastMCP
from services.users import UsersServicer
from db.connection import MongoConnector
from config.env import EnvConfig

mcp = FastMCP("chatbot-server")

urlMongo = EnvConfig().get("MONGO_URL")
connector = MongoConnector(urlMongo, "competition_manager")
users_service = UsersServicer(connector)

# ? --------------------------------------------- Herramientas relacionadas con usuarios ---------------------------------------------

@mcp.tool("count_users_by_type")
async def count_users_by_type():
    try:
        result = await users_service.count_by_type()
        return result if result else {"message": "No se encontraron tipos de usuario."}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("total_users")
async def total_users():
    try:
        result = await users_service.total_users()
        return {"total": result}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("users_by_location")
async def users_by_location():
    try:
        result = await users_service.users_by_location()
        return result if result else {"message": "No se encontraron ubicaciones de usuario."}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("registered_after")
async def registered_after(year: int):
    try:
        result = await users_service.registered_after(year)
        return {"año": year, "total": result}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("last_purchase_in_year")
async def last_purchase_in_year(year: int):
    try:
        result = await users_service.last_purchase_in_year(year)
        return {"año": year, "total": result}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("buyers_in_location")
async def buyers_in_location(location: str):
    try:
        result = await users_service.buyers_in_location(location)
        return {"ubicacion": location, "total": result}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool("registered_in_company_year")
async def registered_in_company_year(empresa: str, year: int):
    try:
        result = await users_service.registered_in_company_year(empresa, year)
        return {"empresa": empresa, "año": year, "total": result}
    except Exception as e:
        return {"error": str(e)}


# ? --------------------------------------------- herramientas relacionadas con las compañías ---------------------------------------------



if __name__ == "__main__":
    mcp.run(transport="streamable-http")