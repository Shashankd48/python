from pymongo import MongoClient

# Create a MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
db = client["leads_generation"]

# Access a specific collection
collection = db["Users"]

# Perform database operations
# ...

documents = collection.find()
for document in documents:
    print(document)

# Close the MongoDB connection
client.close()
