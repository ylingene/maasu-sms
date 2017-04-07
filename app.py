from flask import Flask, request
from twilio import twiml
import string
import unicodedata


app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	message_body = unicodedata.normalize('NFKD', message_body).encode('ascii','ignore')
	message_body = message_body.lower().replace(" ", "").translate(None, string.punctuation)

	if message_body == "banquet":
		message = "Saturday's banquet will be held at The Diamond Center of Novi (46100 Grand River Ave, Novi, MI 48374). Food and entertainment will be provided. Buses for banquet (if requested) will be leaving at 6:30PM. Reply 'bus' for more bus information.";
	elif message_body == "friday":
		message = "We have two events for you on Friday Night: Spring Into MAASU and GenAPA. Reply 'spring' or 'genapa' for more info.";
	elif message_body == "easthall":
		message = "East Hall is where our Friday night entertainment, Spring Into MAASU, is located. Address: 530 Church St, Ann Arbor, MI 48109";
	elif message_body == "masonhall":
		message = "Mason Hall will be where all workshops and small group sessions are located. Address: 419 S State St Mason Hall, Ann Arbor, MI 48109";
	elif message_body == "rackham":
		message = "Rackham Auditorium will house our opening ceremony as well as Saturday morning registration. Address: 915 E Washington St, Ann Arbor, MI 48109";
	elif message_body == "maasu":
		message = """Here are the commands I accept: 
					\n'parking': parking information
					\n'friday': Friday night information
					\n'spring': Spring Into Maasu Friday night event
					\n'genapa': GenAPA Friday night show information 
					\n'banquet': banquet information
					\n'easthall': address for East Hall (Friday night entertainment and Friday registration)
					\n'masonhall': address for Mason Hall (all workshops)
					\n'rackham': address for Rackham Auditorium (Opening ceremony and Saturday registration)
					\n'bus': bus information
		"""
	elif message_body == "bus":
		message = "Buses will begin boarding at 6PM and will depart at 6:30PM. Pickup location is on the corner of N University Ave. and S State St.";
	elif message_body == "parking":
		message = "Parking will be $10 for the day at the Thayer Parking Structure. Address: 216 South Thayer Street, Ann Arbor, MI 48104";
	elif message_body = "genapa":
		"The GenAPA show is from 7-9pm Friday night. You can pick up reserved tickets or purchase them at the door outside of Mendelssohn Theater at the Michigan League (Address: 911 N University Ave, Ann Arbor, MI 48104) starting at 6:30pm. We suggest you get there by 6:30";
	elif message_body = "spring":
		"Spring Into Maasu goes from 8:30-10:00pm at East Hall Psych Atrium (Address: 530 Church St, Ann Arbor, MI 48109). There will be free food and activites after registration. Ask your Small Group Leader for more information.";
	else:
		message = """Here are the commands I accept: 
					\n'parking': parking information
					\n'friday': Friday night information
					\n'spring': Spring Into Maasu Friday night event
					\n'genapa': GenAPA Friday night show information 
					\n'banquet': banquet information
					\n'easthall': address for East Hall (Friday night entertainment and Friday registration)
					\n'masonhall': address for Mason Hall (all workshops)
					\n'rackham': address for Rackham Auditorium (Opening ceremony and Saturday registration)
					\n'bus': bus information
		"""

	print message_body
	resp = twiml.Response()
	resp.message(message)
	return str(resp)

def remove_number(number):
	return
 
if __name__ == '__main__':
    app.run()