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
		message = "Saturday's banquet will be held at The Diamond Center of Novi (46100 Grand River Ave, Novi, MI 48374). Food and entertainment will be provided. Buses for banquet (if requested) will be leaving at 6:30PM. Reply 'bus' for more bus information."
	elif message_body == "friday":
		message = ""
	elif message_body == "easthall":
		message = "easthall"
	elif message_body == "masonhall":
		message = "masonhall"
	elif message_body == "rackham":
		message = "rackham"
	elif message_body == "united":
		message = """Here are the commands I accept: 
					\n'friday': friday night information
					\n'banquet': banquet information
					\n'east hall': address for East Hall (Friday night entertainment and Friday registration)
					\n'mason hall': address for Mason Hall (all workshops)
					\n'rackham': address for Rackham Auditorium (Opening ceremony and Saturday registration)
					\n'bus': bus information
		"""
	elif message_body == "bus":
		message = "bus"
	else:
		message = """Here are the commands I accept: 
					\n'friday': friday night information
					\n'banquet': banquet information
					\n'east hall': address for East Hall (Friday night entertainment and Friday registration)
					\n'mason hall': address for Mason Hall (all workshops)
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