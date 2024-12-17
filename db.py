# import motor.motor_asyncio
# from dotenv import load_dotenv
# import os

# load_dotenv()

# DB_PASS = os.environ.get("DB_PASS")

# MONGO_DETAILS = f"mongodb+srv://huzaifarehan:{DB_PASS}@cluster0.bvyuobe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# MONGO_DETAILS = "mongodb+srv://huzaifarehan:Pcx1DKDOjvXsJPE3@cluster0.bvyuobe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MONGO_DETAILS_ABDULAHAD = "mongodb://localhost:27017/"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS_ABDULAHAD)
# database = client.plantApp
# user_collection = database.users
import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()
# private_key= "d1152977-a17e-4be0-acf4-b60e69d7f67d"
DB_PASS = os.environ.get("DB_PASS")
MONGO_DETAILS_ABDULAHAD = "mongodb+srv://khanabdulahadmuhammad:July%3A20022002@cluster0.aqwds37.mongodb.net/"

try:
    # Try connecting to the database
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS_ABDULAHAD)
    database = client.plantApp
    user_collection = database.users
    plant_collection = database.plants
    
    # Test connection
    print("Database connected successfully!")
    
except Exception as e:
    print(f"Error connecting to the database: {str(e)}")
