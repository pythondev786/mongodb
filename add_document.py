from pymongo import MongoClient

DB_URI = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.9'
db_name = "test_db"
collection_name =  "users"

def add_document(document: dict):
    """
    Adds a document to a MongoDB collection.
    
    :param document: Dictionary representing the document to insert
    :return: Inserted document ID
    """
    try:
        client = MongoClient(DB_URI)
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_one(document)
        print(result)
        return result.inserted_id
    except Exception as e:
        return f"Error: {e}"
    finally:
        client.close()

# Example usage:
document_id = add_document({"name": "John", "age":30})
print("Inserted document ID:", document_id)
