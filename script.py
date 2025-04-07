import pymongo
import requests
from dotenv import load_dotenv
import os
from generate_embedding import generate_embedding
load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

db = client.genaiDB

collection = db.movies
    

queries = [
    "Avengers: Endgame",
    "movie about a hidden advanced kingdom",  
    "funny space adventure with criminals",  
]

for query in queries:
    print(f"\nSearching for: '{query}'")
    results = collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": generate_embedding(query),
                "path": "embedding",
                "numCandidates": 100,
                "limit": 5,
                "index": "vector_index",
            }
        }
    ])
    
    print("Results:")
    for document in results:
        print(f"Movie: {document['title']} - Description: {document['description']}")





