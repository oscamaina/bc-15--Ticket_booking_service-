import sys
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

def create_event(name, start, end, venue):
	event_name = arg['<name>']
	start_date = datetime.strptime (arg['<start_date>'], "%y/%m/%d") 
	end_date = datetime.strptime (arg['<end_date>'], "%y/%m/%d")
	venue = arg['<venue>']
	
	new_event = Events(name=event_name,start_date=start_date, end_date=end_date,venue=venue)

	session.add(new_event)
	session.commit()
	return "Created event"

def delete_event(self):
	deleted = session.query(Events).filter_by(id="event_id")
	session.delete(deleted)
	session.commit()
	return "Deleted event"

def list(self):
	evts = session.query(Events).all()