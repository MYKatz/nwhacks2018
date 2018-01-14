#!/usr/local/bin/python
import json
from get_twilio_info import read
from flask import Flask
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather, Say

#Construct Twilio Client
inf = read("hacksnw123")
t_client = Client(inf[0],inf[1])

#Construct MongoDB Client
from pymongo import MongoClient
m_client = MongoClient()

#read mongo db
to = ''
from_ = ''
url = ''

call = t_client.calls.create(
    to="+17789568798",
    from_="+16046708545",
    url="http://demo.twilio.com/docs/voice.xml"
)

app = Flask(__name__)
@app.route("/voice", methods=['GET', 'POST'])

def validate(phone,true_code,_num_digits=6,_timeout=10):
	"""Respond to incoming phone calls with a menu of options"""
	# Start our TwiML response
	resp = VoiceResponse()
	# Start our <Gather> verb
	# num_digits is how many digits in authentication
	inp = Gather(num_digits=_num_digits,timeout=_timeout)
	inp.say('Please enter your 6 digit passcode.')
	resp.append(inp)
	# If the user doesn't select an option, redirect them into a loop
	resp.redirect('/voice')
	return str(resp) == true_code

if __name__ == "__main__":
    app.run(debug=True)
