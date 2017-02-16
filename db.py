
import sys
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

base = declarative_base()

engine = create_engine('sqlite:///./database.db')

Session = sessionmaker(bind=engine)
session = Session()

class Events(base):

	__tablename__ = 'events'

	event_id = Column(Integer, primary_key=True)
	name = Column(String(255), unique=True)
	start_date = Column(DateTime())
	end_date = Column(DateTime())
	venue = Column(String(255))

class Tickets(base):
	__tablename__ = 'tickets'

	t_id = Column(Integer, primary_key=True)
	event_name = Column(String(255))
	t_type = Column(String(255))
	t_status = Column(String(255))


base.metadata.create_all(engine)