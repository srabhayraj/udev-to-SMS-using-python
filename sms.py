#!/usr/bin/python36
import time 
from time import sleep 
from sinchsms import SinchSMS 

def sendSMS(): 

	# enter all the details 
	# get app_key and app_secret by registering 
	# a app on sinchSMS 
	number = '+917877781344'
	app_secret = 'P0q02HeH60OMMKokwb/xkw=='
	app_key = '378cb6cd-5655-4108-8172-fd3474fb6e3a'

	# enter the message to be sent 
	message = 'Hey Ravi! Someone plugged a usb device in your system'

	client = SinchSMS(app_key, app_secret) 
	print("Sending '%s' to %s" % (message, number)) 

	response = client.send_message(number, message) 
	message_id = response['messageId'] 
	response = client.check_status(message_id) 

	# keep trying unless the status retured is Successful 
	while response['status'] != 'Successful': 
		print(response['status']) 
		time.sleep(1) 
		response = client.check_status(message_id) 

	print(response['status']) 

if __name__ == "__main__": 
	sendSMS() 

