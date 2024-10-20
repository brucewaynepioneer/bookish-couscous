# some_database_module.py
from pymongo import MongoClient

# Establish a connection to MongoDB using the connection string from __init__.py
MONGODB_CONNECTION_STRING = config("MONGODB")

mongo_client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

def load_delete_words(user_id: int):
    """
    Load the delete words list for a specific user from MongoDB.
    
    :param user_id: Telegram user ID
    :return: A list of delete words for the user
    """
    user_data = collection.find_one({"user_id": user_id}, {"_id": 0, "delete_words": 1})
    if user_data and "delete_words" in user_data:
        return user_data["delete_words"]
    return []

def save_replacement_words(user_id: int, replacements: dict):
    """
    Save the replacement words for a user in MongoDB.
    
    :param user_id: Telegram user ID
    :param replacements: A dictionary of old words as keys and new words as values
    """
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"replacements": replacements}},
        upsert=True  # Insert the user document if it doesn't exist
    )

def save_filename_replacement(user_id: int, old_filename: str, new_filename: str):
    """
    Save the filename replacement for a user in MongoDB.
    
    :param user_id: Telegram user ID
    :param old_filename: The old filename that needs to be replaced
    :param new_filename: The new filename to replace the old one
    """
    collection.update_one(
        {"user_id": user_id},
        {"$set": {f"filename_replacements.{old_filename}": new_filename}},
        upsert=True
    )
