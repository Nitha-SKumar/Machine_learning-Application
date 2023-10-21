import pandas as pd
import pymongo
import json
#from pymongo.mongo_client import MongoClient

client = "mongodb+srv://Nitha:Shivbaba@cluster0.6tmpzbq.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"/Users/nitha/Downloads/ML Bootcamp/Machine_learning-Application/src/Data/train.csv")
DATABASE ="MAchine_learning"
COLLECTION_NAME ="DATASET"
if __name__ =="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns of our data: {df.shape}")
    
    df.reset_index(drop =True, inplace =True)
    joson_record =list(json.loads(df.T.to_json()).values())
    
    print(joson_record[0])
    
    client[DATABASE][COLLECTION_NAME].insert_many(joson_record)
    
    