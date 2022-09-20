from typing import List, Union

from pydantic import BaseModel


class ItemCreate():
    pass


class Item(BaseModel):
    id: int
    name:str 
    db_letter:str
    transportation:float
    retailable:bool 
    research:bool
    realmAvailable:bool 
    producedAnHour:float
    averageRetailPrice:float
    marketSaturation:float
    marketSaturationLabel:str
    retailModeling:str 
    neededFor:str 
    producedFrom:str 
    producedAt:str 
    lowestMarketPrice:float  

    class Config:
        orm_mode = True


class BuildingBase(BaseModel):
    email: str


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True