import urllib.request
import json

endPoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5ml_LjqDuOKTKLBke4Q9de-6GVy4'

orgin = input('Where are you?: ').replace(' ', '+')
destination = input('Where do you want to go?: ')

nav_request = 'orgin=()&destination=(]'.format(orgin, destination, api_key)

request = endPoint + nav_request

response = urllib.request.urlopen(request).read()

directions = json.loads(response)

print(directions)