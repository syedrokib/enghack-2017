from credentials import account_sid, auth_token, my_cell, my_twilio
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json, urllib
from urllib.parse import urlencode
import googlemaps
import re

app = Flask(__name__)

@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
	
	resp = MessagingResponse()
	
	#Fix origin. Start and end destinations.
	origin = '280 Simcoe St, Toronto, ON'
	destination = request.values.get('Body', None)
	
	#converts to string form appropriate for the address bar with plus signs
	origin = origin.replace(' ', '+')
	destination = destination.replace(' ', '+')
	
	key = 'AIzaSyB6ZKzS-IiUPPm13YfGbJr5EgWa_H1yvcg'
	
	url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&key=' + key
	open_url = urllib.request.urlopen(url)
	response = json.load(open_url)
	
	#Directions are empty by default and step number starts at 1 by default.
	directions_list = ""
	step_number = 1
	
	for i in range (0, len (response['routes'][0]['legs'][0]['steps'])):
	
		#Fetches instruction.
		instruction = response['routes'][0]['legs'][0]['steps'][i]['html_instructions']
	
		#Converts to following format: 1. (instruction)
		append_this_step = "\n" + str(step_number) + ". " + str(instruction) + "\n"
		step_number += 1
	
		directions_list += append_this_step
	
		#Cleans string.
		#directions_list = str(re.sub("<b>", "", directions_list))
		#directions_list = str(re.sub("</b>", "", directions_list))
		directions_list = str(re.sub("<.*?>", "", directions_list))
		
		if directions_list.endswith('Destination will be on the right\n'):
			directions_list = directions_list.replace('Destination will be on the right\n', '\nDestination will be on the right\n')
		elif directions_list.endswith("Destination will be on the left\n"):
			directions_list = directions_list.replace('Destination will be on the left\n', '\nDestination will be on the left\n')
					
	#Sends string as a text message.
	resp.message(directions_list)	
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug = True)
