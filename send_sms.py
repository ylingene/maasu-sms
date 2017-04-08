# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from twilio import twiml
from os import listdir
from os.path import isfile, join

# Find these values at https://twilio.com/user/account
account_sid = "AC59dfca8ed222792aaa85ebd22d5769cc"
auth_token = "6dbb0fdd812efcd55baa21b69f13ee61"
client = TwilioRestClient(account_sid, auth_token)

FROM_NUMBERS = ['+17342010395',
				'+17342010335',
				'+17342010386',
				'+17342010264',
				'+15866236270',
				'+17342010273',
				'+17342010337',
				'+17342010318',
				'+17342010365',
				'+17342010255']

def sendMessage(_to, _from, msg):
	try:
		message = client.messages.create(to=_to, from_=_from, body=msg)
	except TwilioRestException as e:
		print(e)

onlyfiles = [f for f in listdir('numbers/') if isfile(join('numbers/', f))]
for idx, filename in enumerate(onlyfiles):
	with open('numbers/'+filename) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	_from = FROM_NUMBERS[idx]
	msg="This is a test"
	for to in content:
		sendMessage(to, _from, msg)