import sys
from db import Events
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

base = declarative_base()

engine = create_engine('sqlite:///./database.db')

Session = sessionmaker(bind=engine)
session = Session()
def create_event(name, start, end, venue):
	event_name = name
	start_date = start 
	end_date = end
	venue = venue
	
	new_event = Events(name=event_name,start_date=start_date, end_date=end_date,venue=venue)


	session.add(new_event)
	session.commit()
	return "Created event"

def delete_event(event_id):
	deleted = session.query(Events).filter_by(event_id=event_id).first()
	session.delete(deleted)
	session.commit()
	return "deleted event"

def list():
	evts = session.query(Events).all()
	events_list = []
	for evt in evts:
		print(evt.name + str(evt.start_date) + str(evt.end_date) + evt.venue)
