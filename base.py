from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker



engine = create_engine('sqlite:///simCompaniesDB', echo=True, future=True)

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


   