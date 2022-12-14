
from sqlalchemy import ARRAY, Column, ForeignKey, String, Integer
from base import Base, Session, engine
import json, requests


#- Building class for each building with properties within
class Building(Base):

    __tablename__ = 'Buildings'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    cost = Column(Integer)
    costUnits = Column(Integer)
    wages = Column(Integer)
    secondsToBuild = Column(Integer)
    category = Column(String)
    kind = Column(String)
    robotsNeeded = Column(Integer)
    realmAvailable = Column(Integer)

    def __init__(self, name, image, cost, costUnits, wages, secondsToBuild, category, kind, robotsNeeded, realmAvailable):
        self.name = name
        self.image = image
        self.cost = cost
        self.costUnits = costUnits
        self.wages = wages
        self.secondsToBuild = secondsToBuild
        self.category = category
        self.kind = kind
        self.robotsNeeded = robotsNeeded
        self.realmAvailable = realmAvailable

    def __init__(self, name, image, db_letter, transportation, retailable, research, realmAvailable, anHour, parentBuilding):
        self.name = name
        self.image = image
        self.db_letter = db_letter
        self.transportation = transportation
        self.retailable = retailable
        self.research = research
        self.realmAvailable = realmAvailable
        self.anHour = anHour
        self.parentBuilding = parentBuilding


Base.metadata.create_all(engine) # This method will issue queries that first check for the existence of each individual table, and if not found will issue the CREATE statements
session = Session()



def populateBuildingsTable():
    url = "https://www.simcompanies.com/api/v3/0/buildings/1/"
    response = requests.get(url)
    buildingData = json.loads(response.text)
    for building in buildingData:
        name = building['name']
        image = building['image']
        cost = building['cost']
        costUnits = building['costUnits']
        wages = building['wages']
        secondsToBuild = building['secondsToBuild']
        category = building['category']
        kind = building['kind']
        robotsNeeded = building['robotsNeeded']
        realmAvailable = building['realmAvailable']
        building = Building(name, image, cost, costUnits, wages, secondsToBuild, category, kind, robotsNeeded, realmAvailable)
        session.add(building)
        session.commit()

#print all columns of table Buildings
def printAllBuildings():
    for building in session.query(Building.production).all():
        print(building)

# query all rows of table Production that have a parentBuilding of "Factory"
def printFactoryProduction():
    for production in session.query(Production).filter(Production.parentBuilding == "Factory").all():
        print(production.name)


def printAllBuildingNames():
    for building in session.query(Building).all():
        print(building.name)



printAllBuildingNames()

#populateBuildingsTable()
#populateProductionTable()