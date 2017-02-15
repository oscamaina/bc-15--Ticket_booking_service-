# Ticket_booking_service


The application allows users to create events, delete events and view events. It also allows users to generate event tickets and invalidate tickets. Generated tickets are sent to user's email if uploaded




**Installation**

`$ git clone https://github.com/oscamaina/bc-15-Ticket_booking_service

`$ cd bc-15-Ticket_booking_service`
 
 Create and activate a virtual environment.
 
 ```
 $ virtualenv env
 $ cd venv/Scripts
 & activate
 & cd..
 & cd..
 ```
 
 Install dependencies
 
 `$ pip install -r requirements.txt`




 **Run the app**
 
 ```

 python appy.py

 ```

 **Commands**
 
 ```
    event create <name> <start_date> <end_date> <venue>
    event delete <event_id>
    event edit <event_id> <new_details>
    event list
    event view <event_id>
    ticket generate <email>
    ticket invalidate <ticket_id>

```
 
