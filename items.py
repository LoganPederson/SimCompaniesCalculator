from sqlalchemy import Column, String, Integer
from base import Base, Session, engine
from buildings import Building
import json, requests


#- Item class for each resource with properties within
class Item(Base): 
    
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    db_letter = Column(String)
    transportation = Column(Integer)
    retailable = Column(Integer)
    research = Column(Integer)
    realmAvailable = Column(Integer)
    producedAnHour = Column(Integer)
    averageRetailPrice = Column(Integer)
    marketSaturation = Column(Integer)
    marketSaturationLabel = Column(String)
    retailModeling = Column(String)
    neededFor = Column(String)
    producedFrom = Column(String)
    producedAt = Column(String)
    lowestMarketPrice = Column(Integer)



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



#- generate database schema
Base.metadata.create_all(engine)

#- create a new session
session = Session()

#- GET request from API for specified resource db_letter
def getResourceData(db_letter):
    url = "https://www.simcompanies.com/api/v4/en/0/encyclopedia/resources/0/{}/".format(db_letter)  
    response = requests.get(url)
    resourceData = json.loads(response.text)
    return resourceData

def getMarketData(db_letter):
    url = "https://www.simcompanies.com/api/v3/market/0/{}/".format(db_letter) 
    response = requests.get(url)
    marketData = json.loads(response.text)
    return marketData


#- loop through commodity list and get data from API
def populateItemsTable():
    i = 1
    while i <= 113: 
        if(i <= 35):# 0 to 35
            resourceData = getResourceData(i)
            marketData = getMarketData(i)
            name = resourceData["name"]
            db_letter = resourceData["db_letter"]
            transportation = resourceData["transportation"]
            retailable = resourceData["retailable"]
            research = resourceData["research"]
            realmAvailable = resourceData["realmAvailable"]
            producedAnHour = resourceData["producedAnHour"]
            averageRetailPrice = resourceData["averageRetailPrice"]
            marketSaturation = resourceData["marketSaturation"]
            marketSaturationLabel = resourceData["marketSaturationLabel"]
            retailModeling = resourceData["retailModeling"]
            neededForString = ""
            if "neededFor" in resourceData:
                for item in resourceData["neededFor"]:
                    if item["name"]:
                        neededForString = neededForString + item["name"] + '-'
            producedFromString = ""
            if 'producedFrom' in resourceData:
                # check if producedFrom list is empty
                if len(resourceData["producedFrom"]) > 0:
                    amountToPrint = len(resourceData["producedFrom"])
                    x = 0
                    for item in resourceData["producedFrom"]:
                        print(resourceData["producedFrom"][x])
                        if x < amountToPrint:
                            producedFromString = producedFromString + resourceData["producedFrom"][x]["resource"]["name"] + "+"+str(resourceData["producedFrom"][x]["amount"])+"-"
                            x = x + 1
            producedAtString = ""
            if 'producedAt' in resourceData:
                producedAtString = producedAtString + resourceData["producedAt"]["name"]
            neededFor = neededForString
            producedFrom = producedFromString
            producedAt = producedAtString
            lowestMarketPrice = marketData[0]["price"]
            newItem = Item(name, db_letter, transportation, retailable, research, realmAvailable, producedAnHour, averageRetailPrice, marketSaturation, marketSaturationLabel, retailModeling, neededFor, producedFrom, producedAt, lowestMarketPrice)
            session.add(newItem)
        if(i >= 40 and i <= 89): # 40 to 89
            resourceData = getResourceData(i)
            marketData = getMarketData(i)
            name = resourceData["name"]
            db_letter = resourceData["db_letter"]
            transportation = resourceData["transportation"]
            retailable = resourceData["retailable"]
            research = resourceData["research"]
            realmAvailable = resourceData["realmAvailable"]
            producedAnHour = resourceData["producedAnHour"]
            averageRetailPrice = resourceData["averageRetailPrice"]
            marketSaturation = resourceData["marketSaturation"]
            marketSaturationLabel = resourceData["marketSaturationLabel"]
            retailModeling = resourceData["retailModeling"]
            neededForString = ""
            if "neededFor" in resourceData:
                for item in resourceData["neededFor"]:
                    if item["name"]:
                        neededForString = neededForString + item["name"] + '-'
            producedFromString = ""
            if 'producedFrom' in resourceData:
                # check if producedFrom list is empty
                if len(resourceData["producedFrom"]) > 0:
                    amountToPrint = len(resourceData["producedFrom"])
                    x = 0
                    for item in resourceData["producedFrom"]:
                        print(resourceData["producedFrom"][x])
                        if x < amountToPrint:
                            producedFromString = producedFromString + resourceData["producedFrom"][x]["resource"]["name"] + "+"+str(resourceData["producedFrom"][x]["amount"])+"-"
                            x = x + 1
            producedAtString = ""
            if 'producedAt' in resourceData:
                producedAtString = producedAtString + resourceData["producedAt"]["name"]
            neededFor = neededForString
            producedFrom = producedFromString
            producedAt = producedAtString
            lowestMarketPrice = marketData[0]["price"]
            newItem = Item(name, db_letter, transportation, retailable, research, realmAvailable, producedAnHour, averageRetailPrice, marketSaturation, marketSaturationLabel, retailModeling, neededFor, producedFrom, producedAt, lowestMarketPrice)
            session.add(newItem)
        if(i == 98): # 98
            resourceData = getResourceData(i)
            marketData = getMarketData(i)
            name = resourceData["name"]
            db_letter = resourceData["db_letter"]
            transportation = resourceData["transportation"]
            retailable = resourceData["retailable"]
            research = resourceData["research"]
            realmAvailable = resourceData["realmAvailable"]
            producedAnHour = resourceData["producedAnHour"]
            averageRetailPrice = resourceData["averageRetailPrice"]
            marketSaturation = resourceData["marketSaturation"]
            marketSaturationLabel = resourceData["marketSaturationLabel"]
            retailModeling = resourceData["retailModeling"]
            neededForString = ""
            if "neededFor" in resourceData:
                for item in resourceData["neededFor"]:
                    if item["name"]:
                        neededForString = neededForString + item["name"] + '-'
            producedFromString = ""
            if 'producedFrom' in resourceData:
                # check if producedFrom list is empty
                if len(resourceData["producedFrom"]) > 0:
                    amountToPrint = len(resourceData["producedFrom"])
                    x = 0
                    for item in resourceData["producedFrom"]:
                        print(resourceData["producedFrom"][x])
                        if x < amountToPrint:
                            producedFromString = producedFromString + resourceData["producedFrom"][x]["resource"]["name"] + "+"+str(resourceData["producedFrom"][x]["amount"])+"-"
                            x = x + 1
            producedAtString = ""
            if 'producedAt' in resourceData:
                producedAtString = producedAtString + resourceData["producedAt"]["name"]
            neededFor = neededForString
            producedFrom = producedFromString
            producedAt = producedAtString
            lowestMarketPrice = marketData[0]["price"]
            newItem = Item(name, db_letter, transportation, retailable, research, realmAvailable, producedAnHour, averageRetailPrice, marketSaturation, marketSaturationLabel, retailModeling, neededFor, producedFrom, producedAt, lowestMarketPrice)
            session.add(newItem)
        if(i >= 100): # 100 to 113
            resourceData = getResourceData(i)
            marketData = getMarketData(i)
            name = resourceData["name"]
            db_letter = resourceData["db_letter"]
            transportation = resourceData["transportation"]
            retailable = resourceData["retailable"]
            research = resourceData["research"]
            realmAvailable = resourceData["realmAvailable"]
            producedAnHour = resourceData["producedAnHour"]
            averageRetailPrice = resourceData["averageRetailPrice"]
            marketSaturation = resourceData["marketSaturation"]
            marketSaturationLabel = resourceData["marketSaturationLabel"]
            retailModeling = resourceData["retailModeling"]
            neededForString = ""
            if "neededFor" in resourceData:
                for item in resourceData["neededFor"]:
                    if item["name"]:
                        neededForString = neededForString + item["name"] + '-'
            producedFromString = ""
            if 'producedFrom' in resourceData:
                # check if producedFrom list is empty
                if len(resourceData["producedFrom"]) > 0:
                    amountToPrint = len(resourceData["producedFrom"])
                    x = 0
                    for item in resourceData["producedFrom"]:
                        print(resourceData["producedFrom"][x])
                        if x < amountToPrint:
                            producedFromString = producedFromString + resourceData["producedFrom"][x]["resource"]["name"] + "+"+str(resourceData["producedFrom"][x]["amount"])+"-"
                            x = x + 1
            producedAtString = ""
            if 'producedAt' in resourceData:
                producedAtString = producedAtString + resourceData["producedAt"]["name"]
            neededFor = neededForString
            producedFrom = producedFromString
            producedAt = producedAtString
            lowestMarketPrice = marketData[0]["price"]
            newItem = Item(name, db_letter, transportation, retailable, research, realmAvailable, producedAnHour, averageRetailPrice, marketSaturation, marketSaturationLabel, retailModeling, neededFor, producedFrom, producedAt, lowestMarketPrice)
            session.add(newItem)
        i+=1

# query for all neededFor items
def getNeededForItems(): #getting close
    neededForItems = session.query(Item).all()
    for item in neededForItems:

        #print(item.name+' is neededFor: '+item.neededFor) # neededFor is working
        print(item.name + ' is neededFor: '+item.neededFor) 

def getProducedFromItems(): 
    producedFromItems = session.query(Item).all()
    for item in producedFromItems:
        print(item.name + ' is producedFrom: '+item.producedFrom)

def getProducedAtItems():
    producedAtItems = session.query(Item).all()
    for item in producedAtItems:
        print(item.name + ' is producedAt: '+item.producedAt)

def splitProducedFromString(itemName):
    #print itemNames producedFrom
    item = session.query(Item).all()
    for items in item:
        if items.name == itemName:
            splitByMinus = items.producedFrom.split('-')
            #print(splitByMinus) # for loop and check for empty string within list of tuples to split item names and cost
            return(splitByMinus)

def getLowestMarketPrice(itemName):
    itemTable = session.query(Item).all()
    for item in itemTable:
        if item.name == itemName:
            return item.lowestMarketPrice


# takes (string, int, float%, float%) and outputs dictionary where values are item names and keys are profit per hour of sourcing materials from market, and selling the produced item on the market accounting for 3% fee
def calculateProfitPerHourPerItem(buildingName, buildingLevel, productionModifierPercentage, administrationCostPercentage):
    itemNamesThatCanBeProducuedFromBuilding = session.query(Item).all()
    buildingsTable = session.query(Building).all()
    profitDict = {}
    for item in itemNamesThatCanBeProducuedFromBuilding:
        if item.producedAt == buildingName:
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'+item.name+'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            #print(item.name+': '+str(producedFromMasterList))
            producedFromStringList = splitProducedFromString(item.name)
            print(producedFromStringList)
            totalResourceSourcingCost = 0
            for listItem in producedFromStringList: # ex: [seeds+1,water+4] resourceName+amountNeeded
                if listItem != "":
                    resourceNameAndAmount = listItem.split("+") # ex: [seeds, 1] [water, 4]
                    resourceName = resourceNameAndAmount[0]
                    resourceAmountNeeded = resourceNameAndAmount[1]
                    print(resourceName)
                    print("amount needed: "+str(resourceAmountNeeded))
                    print("lowest market price found: " + str(getLowestMarketPrice(resourceName)))
                    costIncreaseTimesAmountNeeded = (float(getLowestMarketPrice(resourceName))+(float(getLowestMarketPrice(resourceName))*0.03))*float(resourceAmountNeeded) # lowest market price * amount needed to produce item = total sourcing cost from market of this resource for producing 1 unit of item, including 3% market fee on purchase (haven't factored in transportaiton)
                    totalResourceSourcingCost = totalResourceSourcingCost + costIncreaseTimesAmountNeeded
            sourcingCostPerHour = item.producedAnHour * totalResourceSourcingCost
            print("----------------------costPerHour to produce "+str(item.producedAnHour)+" units of "+ item.name + " = " + str(sourcingCostPerHour))
            # get wages from building and use sourcing cost to find profit per item
            for building in buildingsTable:
                if building.name == buildingName:
                    print("BUILDING WAGES --------------------- "+str(building.wages))
                    productionCosts = ((sourcingCostPerHour + (building.wages * buildingLevel)) + ((building.wages*buildingLevel)*administrationCostPercentage))
                    profitPerHour = (getLowestMarketPrice(item.name)*item.producedAnHour) - productionCosts
                    profitDict[item.name]=profitPerHour
                    print("---------------------------------------------Profit per hour!!! = "+str(profitPerHour))
    print(profitDict)
                    

# removes items table
def removeItemsTable():
    session.query(Item).delete()
    session.commit()




calculateProfitPerHourPerItem('Physics laboratory', 1, 1, 0) 

#removeItemsTable()
#populateItemsTable()



#- commit and close session
session.commit()
session.close()

