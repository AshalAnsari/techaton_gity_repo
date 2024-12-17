from fastapi import HTTPException, status,APIRouter, HTTPException, Query
from services.plantServices import identify_plant
from models.plantModel import PlantAdd
from services.plantServices import retrieve_plants, add_plant, retrieve_plant, update_plant, delete_plant
from models.plantModel import PlantAdd, PlantUpdate, PlantSchema, PlantDelete
from models.plantModel import plantIdentify
from data import get_plant_arr

router = APIRouter()

@router.post("/plant/identification", tags=["IMAGE"])
async def get_plant_identification(data:plantIdentify):
    try:
        print("here i am ")
        plant = await identify_plant(data.img)
        return plant
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 
    
@router.get("/plant/find")
async def get_plants_by_temp(temperature: str = Query(None, min_length=1, max_length=10)):
    print(temperature)
    try:
        return get_plant_arr()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 

@router.post("/plants/", status_code=status.HTTP_201_CREATED)
async def create_plant(plant_data: PlantAdd):
    try:
        print("yahan ")
        new_plant = await add_plant(plant_data)
        return new_plant  # Returning the created plant
    except Exception as e:
        # Handle exceptions appropriately
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/plants/", response_model=PlantAdd, status_code=status.HTTP_201_CREATED)
async def create_plant(plant_data: PlantAdd):
    try:
        new_plant = await add_plant(plant_data)
        return new_plant  # Returning the created plant
    except Exception as e:
        # Handle exceptions appropriately
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/plants/", response_model=list[PlantAdd])
async def get_all_plants():
    try:
        plants = await retrieve_plants()
        return plants
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/plants/{plant_id}", response_model=PlantSchema)
async def get_plant(plant_id: str):
    try:
        plant = await retrieve_plant(plant_id)
        if plant:
            return plant
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plant not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/plants/{plant_id}", response_model=PlantSchema)
async def update_plant_data(plant_id: str, plant_data: PlantUpdate):
    try:
        if await update_plant(plant_id, plant_data.dict()):
            updated_plant = await retrieve_plant(plant_id)
            return updated_plant
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Update failed or plant not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/plants/{plant_id}", response_model=PlantDelete)
async def delete_plant_data(plant_id: str):
    try:
        if await delete_plant(plant_id):
            return {"message": "Plant deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plant not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))