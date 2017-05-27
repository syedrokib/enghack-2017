from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

message = "Hello! Please enter your destination. (Example: 100 Yonge St., Toronto, ON)"

client = Client(account_sid, auth_token)
client.messages.create(
	to = my_cell,
	from_ = my_twilio, 
	body = message)