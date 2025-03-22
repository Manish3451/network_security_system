# import os 
# import sys 
# import json 


# from dotenv import load_dotenv
# load_dotenv()


# MONGO_DB_URI = os.getenv("MONGO_DB_URL")

# print(MONGO_DB_URI)

# import certifi
# ca = certifi.where()

# import pandas as pd 
# import numpy as np 
# import pymongo 
# from networksecurity.exception.exception import NetworkSecurityException
# from networksecurity.logging.logger import logging

# class NetworkDataExtract():
#     def __init__(self):
#         try:
#             pass
#         except Exception as e :
#             raise NetworkSecurityException(e,sys)
        
#     def cv_to_json_converter(self,file_path):
#         try:
#             data = pd.read_csv(file_path)
#             data.reset_index(drop = True,inplace=True)
#             records = list(json.loads(data.T.to_json()).values())
#         except Exception as e :
#             raise NetworkSecurityException(e,sys)
        
#     def insert_data_mongodb(self,records,database,collection):
#         try:
#             self.database=database
#             self.collection=collection
#             self.records=records

#             self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
#             self.database = self.mongo_client[self.database]

#             self.collection = self.database[self.collection]
#             self.collection.insert_many(self.records)
#             return(len(self.records))
#         except Exception as e:
#             raise NetworkSecurityException(e,sys)
        


# if __name__=='__main__':
#     FILE_PATH = "Network_Data\phisingData.csv"
#     DATABASE = "MANISHAI"
#     Collection = "NetworkData"
#     networkobj = NetworkDataExtract()
#     records = networkobj.csv_to_json_converter(file_path = FILE_PATH)
#     no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
#     print(no_of_records)


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://manish:sachin123@cluster0.z5gni.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



