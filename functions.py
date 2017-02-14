import sys
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

def create_event(name, start, end, venue):
	event_name = ['<name>']
	start_date = datetime.datetime.strptime (['<start_date>'], "%Y/%m/%d") 
	end_date = datetime.datetime.strptime (['<end_date>'], "%Y/%m/%d")
	venue = ['<venue>']
	
	new_event = Events(name=event_name,start_date=start_date, end_date=end_date,venue=venue)

	session.add(new_event)
	session.commit()
	return "Created event"

