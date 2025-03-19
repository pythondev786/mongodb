from pymongo import MongoClient

DB_URI = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.9'
db_name = "test_db"
collection_name =  "users"

def find_document(query: dict, projection: dict):
    """
    Adds a document to a MongoDB collection.
    
    :param query: Dictionary representing mongodb query
    :projection: Dictionary representing the fields to be included in the returned document
    :return: document
    """
    try:
        client = MongoClient(DB_URI)
        db = client[db_name]
        collection = db[collection_name]
        result = collection.find_one(query, projection)
        print(result)
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        client.close()

# Example usage:
document_id = find_document({"name": "John"}, {"_id":0})
print("Document:", document_id)
