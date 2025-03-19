from pymongo import MongoClient

DB_URI = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.9'

def add_document(db_name: str, collection_name: str, document: dict):
    """
    Adds a document to a MongoDB collection.
    
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param document: Dictionary representing the document to insert
    :param uri: MongoDB connection URI (default: localhost)
    :return: Inserted document ID
    """
    try:
        client = MongoClient(DB_URI)
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id
    except Exception as e:
        return f"Error: {e}"
    finally:
        client.close()

# Example usage:
document_id = add_document("test_db", "users", {"name": "John", "age": 30})
print("Inserted document ID:", document_id)
