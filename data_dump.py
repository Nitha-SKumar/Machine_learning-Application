import pandas as pd
import pymongo
import json

# MongoDB connection URI
uri = "mongodb+srv://Nitha:nitha123@cluster0.6tmpzbq.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = r"/Users/nitha/Downloads/ML Bootcamp/Data/train.csv"
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    # Read data from the CSV file into a Pandas DataFrame
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Convert the DataFrame to a list of dictionaries (JSON records)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    # Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    # Insert the JSON records into the collection
    collection.insert_many(json_records)

    # Close the MongoDB connection
    client.close()
