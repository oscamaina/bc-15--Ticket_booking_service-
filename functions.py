import sys
from db import Events, Tickets
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from mail import sent_mail

class Functions():
	base = declarative_base()

	engine = create_engine('sqlite:///./database.db')

	Session = sessionmaker(bind=engine)
	session = Session()
	events = []


	
	stmt = session.query(Events)
	q = stmt.all()
	for evens in q:
		events.append(evens.name)

	def create_event(self, name, start, end, venue):
		event_name = name
		start_date = start 
		end_date = end
		venue = venue

		if name in self.events:
			return "Event already exists: "
		else:

			new_event = Events(name=event_name,start_date=start_date, end_date=end_date,venue=venue)

			self.session.add(new_event)
			self.session.commit()
			return "Created event"

	def delete_event(self, event_id):
		deleted = self.session.query(Events).filter_by(event_id=event_id).first()
		self.session.delete(deleted)
		self.session.commit()
		return "deleted event"

	def list(self):
		evts = self.session.query(Events).all()
		events_list = []
		for evt in evts:
			print(evt.name + str(evt.start_date) + str(evt.end_date) + evt.venue)

	def view_event(self, event_id):
		output = ""
		statement = self.session.query(Events).filter_by(event_id=event_id).first()
		if statement:
			event_name = statement.name
			stmt = self.session.query(Tickets).filter_by(event_name=event_name).all()
			for ticket in stmt:
				output += (str(ticket.t_id) + ",")
			if output == "":
				return "No tickets for this event"

			return output
		return "Event not found"

	def update_event(self, event_id, name, start_date, end_date, venue):
		updated = update(Events).where(Events.event_id == event_id).values\
		({'name': name, 'start_date': start_date, 'end_date': end_date, 'venue': venue})
		self.session.execute(updated)
		self.session.commit()
		return "updated event"

	def generate_ticket(self, email):
		event_name = input("Enter event name:")
		if event_name in self.events:
			ticket_type = input("Enter V for VIP ticket or R for Regular:")
			if ticket_type.upper() == "V":
				ticket_type = "VIP"
			elif ticket_type.upper() == "R":
				ticket_type = "Regular"
			else:
				return "Invalid ticket choice"
			if ticket_type == "VIP" or ticket_type == "Regular":

				new_ticket = Tickets(event_name=event_name, t_type=ticket_type, t_status="Valid")
				self.session.add(new_ticket)
				self.session.commit()
				ticket_id = new_ticket.t_id
				return sent_mail(email,ticket_id)

		else:
			return "Event doesn't exist"

	def invalidate_ticket(self, t_id):
		statement = update(Tickets).where(Tickets.t_id == t_id).values({'t_status': 'Invalid'})
		self.session.execute(statement)
		self.session.commit()
		return "Ticket number " + str(t_id) + " is now invalidated"