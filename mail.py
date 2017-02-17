import smtplib
from termcolor import colored

def sent_mail(to, ticket_num):
	content = 'Your ticket has been generated, ticket number is ' + str(ticket_num)
	mail = smtplib.SMTP('smtp.gmail.com', 587)

	mail.ehlo()
	mail.starttls()
	mail.login('email', 'password')
	mail.sendmail('email',to,content)

	mail.close()

	return colored("mail sent succesfully", 'green')
