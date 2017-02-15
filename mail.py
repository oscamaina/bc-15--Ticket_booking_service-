import smtplib

def sent_mail(to, ticket_num):
	content = 'Your ticket has been generated, ticket number is ' + str(ticket_num)
	mail = smtplib.SMTP('smtp.gmail.com', 587)

	mail.ehlo()
	mail.starttls()
	mail.login('mainaoscar40@gmail.com', 'maina6484')
	mail.sendmail('mainaoscar40@gmail.com',to,content)

	mail.close()

	return "mail sent succesfully"