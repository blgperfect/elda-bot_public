#ici ce trouve la connexion principal de mongo , ajoute les collections au fur et a mesure.
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI     = os.getenv("MONGO_URI") #config dans .env
DATABASE_NAME = os.getenv("DATABASE_NAME") #config dans .env

mongo_client = AsyncIOMotorClient(MONGO_URI)
db           = mongo_client[DATABASE_NAME]

# Collection pour les config
soutien_collection = db["soutien"]
images_only_collection = db["images_only"]
role_config_collection = db["role_config"]
blacklist_collection    = db["blacklist"]
confession_collection = db["confession_data"]
role_panel_collection = db["role_panels"]