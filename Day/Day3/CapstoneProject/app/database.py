#THIS FILE IS USED TO CONNECT TO THE MONGODB DATABASE 
# and PING IT TO CHECK IF IT IS CONNECTED OR NOT
from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings

#
client: MongoClient = MongoClient(settings.MONGO_URI)
database: Database = client[settings.MONGO_DB_NAME]

#sends a ping command to mongodb to confirm tht the connection is established
def ping_database() -> bool:
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False