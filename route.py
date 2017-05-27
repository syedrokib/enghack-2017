import json, urllib
from urllib.parse import urlencode
import googlemaps
import re

origin = '280 Simcoe St, Toronto, ON'
destination = 'University of Toronto'

#converts to string form appropriate for the address bar with plus signs
origin = origin.replace(' ', '+')
destination = destination.replace(' ', '+')

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&key=AIzaSyB6ZKzS-IiUPPm13YfGbJr5EgWa_H1yvcg'
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
    directions_list = str(re.sub("<b>", "", directions_list))
    directions_list = str(re.sub("</b>", "", directions_list))

