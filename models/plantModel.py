from pydantic import BaseModel, Field
from typing import Optional

class plantBase(BaseModel):
    img : str

class plantIdentify(BaseModel):
    img : str
    
class plantSchema(plantBase):
    id: str = Field(None, example="507f1f77bcf86cd799439011")

class PlantAdd(BaseModel):
    plant_name: str
    plant_image: str
    temperature: str
    lighting: str
    humidity: str
    plant_type: str
    sun_exposure: str
    soil_type: str
    soil_ph: str
    hardiness_zones: str
    native_area: str
    toxicity: str
    common_name: str
    difficulty: str

class PlantUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Updated Plant Name")

class PlantSchema(BaseModel):
    id: str = Field(None, example="507f1f77bcf86cd799439011")
    name: str
    img: str
    temperature: str
    lighting: str
    humidity: str
    plant_type: str
    sun_exposure: str
    soil_type: str
    soil_ph: str
    hardiness_zones: str
    native_area: str
    toxicity: str
    common_name: str
    difficulty: str

class PlantDelete(BaseModel):
    message: str