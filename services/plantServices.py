from utils import bufferToBinary
from predict import predict
from data import get_plant_dict
from models.plantModel import PlantAdd
from db import plant_collection
from bson import ObjectId

async def identify_plant(img:str):
    binaryImg = await bufferToBinary(img)
    class_name = predict(binaryImg)
    return get_plant_dict(class_name)


def plant_helper(plant) -> dict:
    return {
        "plant_name": plant["plant_name"],
        "plant_image": plant["plant_image"],
        "temperature": plant["temperature"],
        "lighting": plant["lighting"],
        "humidity": plant["humidity"],
        "plant_type": plant["plant_type"],
        "sun_exposure": plant["sun_exposure"],
        "soil_type": plant["soil_type"],
        "soil_ph": plant["soil_ph"],
        "hardiness_zones": plant["hardiness_zones"],
        "native_area": plant["native_area"],
        "toxicity": plant["toxicity"],
        "common_name": plant["common_name"],
        "difficulty": plant["difficulty"]
    }



async def retrieve_plants():
    plants = []
    async for plant in plant_collection.find():
        plants.append(plant_helper(plant))
    return plants

async def add_plant(plant_data: PlantAdd) -> dict:
    try:
        # Convert Pydantic model to dictionary
        plant_data_dict = plant_data.dict()
        plant = await plant_collection.insert_one(plant_data_dict)
        new_plant = await plant_collection.find_one({"_id": plant.inserted_id})
        return plant_helper(new_plant)
    except Exception as e:
        # Handle exceptions appropriately
        raise e

async def retrieve_plant(plant_id: str) -> dict:
    plant = await plant_collection.find_one({"_id": ObjectId(plant_id)})
    if plant:
        return plant_helper(plant)

async def update_plant(plant_id: str, data: dict):
    plant = await plant_collection.find_one({"_id": ObjectId(plant_id)})
    if plant:
        updated_plant = await plant_collection.update_one(
            {"_id": ObjectId(plant_id)}, {"$set": data}
        )
        if updated_plant:
            return True
        return False

async def delete_plant(plant_id: str):
    plant = await plant_collection.find_one({"_id": ObjectId(plant_id)})
    if plant:
        await plant_collection.delete_one({"_id": ObjectId(plant_id)})
        return True
