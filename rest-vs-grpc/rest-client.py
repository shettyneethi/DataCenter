from __future__ import print_function
import requests
import json
import sys
from time import perf_counter 

addr = 'http://'+sys.argv[1]+':5000'
api = sys.argv[2]
n = int(sys.argv[3])

response = ""

if api == ( "add" ):
	# Start the stopwatch / counter 
	t1_start = perf_counter()
	for i in range(n):
		response = requests.get(addr+"/api/add/10/2") 
	# Stop the stopwatch / counter 
	t1_stop = perf_counter() 

elif api == ("image"):
	# prepare headers for http request
	headers = {'content-type': 'image/png'}
	img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
	# send http request with image and receive response
	image_url = addr + '/api/image'

	# Start the stopwatch / counter 
	t1_start = perf_counter()
	for i in range(n):
		response = requests.post(image_url, data=img, headers=headers)
	t1_stop = perf_counter()
else:
	print("Invalid api name given")
	sys.exit(0)
 
print("Total Elapsed time during all calls in seconds:",t1_stop-t1_start) 
print("Elapsed avg time for call in mili-seconds:",(((t1_stop-t1_start)/n)*1000) )
	
# # decode response
print("Response of API is", response)
print(json.loads(response.text))