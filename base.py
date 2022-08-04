from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings


def getEngine(user, passwd, host, port, db):
    url = f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        print("database does not exist?!!")
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=True) # Change echo for more or less printout I assume
    return engine


    
#engine = create_engine('sqlalchemy:///simcompaniescalculator.c4w8wmvikrna.us-east-2.rds.amazonaws.com', echo=True, future=True)

engine = getEngine(
    settings['pguser'],
    settings['pgpasswd'],
    settings['pghost'],
    settings['pgport'],
    settings['pgdb'])

# print(
#     settings['pguser'],
#     settings['pgpasswd'],
#     settings['pghost'],
#     settings['pgport'],
#     settings['pgdb'])

Session = sessionmaker(bind=engine) 
Base = declarative_base() 

'''
declarative_base() callable returns a new base class from which all mapped classes should inherit. 
When the class definition is completed, a new Table and mapper() will have been generated.
The resulting table and mapper are accessible via __table__ and __mapper__ attributes
'''





#- generate database schema
Base.metadata.create_all(engine)




# #- create a new session
# session = Session()

# #delete table items
# session.execute(text("DROP TABLE Items"))


   