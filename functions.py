import sys
from db import Events, Tickets
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from mail import sent_mail
from tabulate import tabulate
from termcolor import colored
from sqlalchemy.orm.exc import UnmappedInstanceError

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

		""" Creates new event """

		event_name = name
		start_date = start 
		end_date = end
		venue = venue

		if name in self.events:
			return colored ("Event already exists: ", 'red')
		else:

			new_event = Events(name=event_name,start_date=start_date, end_date=end_date,venue=venue)
			self.events.append(event_name)
			self.session.add(new_event)
			self.session.commit()
			return colored("Created event " + new_event.name + " successfully", 'green')

	def delete_event(self, event_id):

		""" Deletes event specified with event_id """

		try:
			deleted = self.session.query(Events).filter_by(event_id=event_id).first()
			self.session.delete(deleted)
			self.session.commit()
			return colored("Event successfully deleted", 'red')
		except UnmappedInstanceError:
			return colored("Event id doesn't exist", 'red')

	def list(self):

		""" Lists all the events in the database """

		evts = self.session.query(Events).all()
		events_list = []
		length = 0
		for evt in evts:
			eventss = [evt.event_id,evt.name,evt.start_date,evt.end_date,evt.venue]
			events_list.append(eventss)
			length = len(events_list)
		if length > 0:
			print(colored(tabulate(events_list, headers=['Event id','Event Name', 'Start date', 'End date', 'Venue'],\
					tablefmt='fancy_grid'), 'cyan'))
		else:
			print (colored("There are no available lists", "red"))

	def view_event(self, event_id):

		""" Lists all tickets for event of event_id """

		output = ""
		statement = self.session.query(Events).filter_by(event_id=event_id).first()
		if statement:
			event_name = statement.name
			stmt = self.session.query(Tickets).filter_by(event_name=event_name).all()
			for ticket in stmt:
				output += (str(ticket.t_id) + ",")
			if output == "":
				return colored("No available tickets for this event", 'red')

			return output
		return colored("Event not found", 'red')

	def update_event(self, event_id, name, start_date, end_date, venue):

		""" Edits an already existing event in the database """

		updated = update(Events).where(Events.event_id == event_id).values\
		({'name': name, 'start_date': start_date, 'end_date': end_date, 'venue': venue})
		self.session.execute(updated)
		self.session.commit()
		return colored("successfully updated " + name + " event", 'green')

	def generate_ticket(self, email):

		""" Generates ticket and sent to specified email """

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
			return colored("Event doesn't exist", 'red')

	def invalidate_ticket(self, t_id):

		""" Invalidates a ticket """
		
		statement = update(Tickets).where(Tickets.t_id == t_id).values({'t_status': 'Invalid'})
		self.session.execute(statement)
		self.session.commit()
		return colored("Ticket number " + str(t_id) + " is now invalidated", 'red')