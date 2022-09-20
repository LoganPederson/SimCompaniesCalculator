from sqlalchemy import Column, String, Integer, Boolean, Float
from base import Base, Session, engine
from buildings import Building
import json, requests
from time import sleep

#- Item class for each resource with properties within
class Item(Base): 
    
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    db_letter = Column(String)
    transportation = Column(Float)
    retailable = Column(Boolean)
    research = Column(Boolean)
    realmAvailable = Column(Boolean)
    producedAnHour = Column(Float)
    averageRetailPrice = Column(Float)
    marketSaturation = Column(Float)
    marketSaturationLabel = Column(String)
    retailModeling = Column(String)
    neededFor = Column(String)
    producedFrom = Column(String)
    producedAt = Column(String)
    lowestMarketPrice = Column(Float)



    def __init__(self, name, db_letter, transportation, retailable, research, realmAvailable, producedAnHour, averageRetailPrice,marketSaturation,marketSaturationLabel,retailModeling, neededFor, producedFrom, producedAt, lowestMarketPrice):
        self.name = name
        self.db_letter = db_letter
        self.transportation = transportation
        self.retailable = retailable
        self.research = research
        self.realmAvailable = realmAvailable
        self.producedAnHour = producedAnHour
        self.averageRetailPrice = averageRetailPrice
        self.marketSaturation = marketSaturation
        self.marketSaturationLabel = marketSaturationLabel
        self.retailModeling = retailModeling
        self.neededFor = neededFor
        self.producedFrom = producedFrom
        self.producedAt = producedAt
        self.lowestMarketPrice = lowestMarketPrice