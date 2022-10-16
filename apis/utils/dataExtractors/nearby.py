import requests
import json

def nearbyTypeCollector(query,lat,lon,radius):
	"""
	Function to search places given a query using text_search from places API
	"""
	# Position
	location = f'{lat},{lon}'	
	# API GOOGLE
	API_KEY = requests.get('http://localhost:5000/keys/GOOGLE_MAPS_KEY').text
	
	# Endpoint
	endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'	
	# Parameters
	params = {
	    'type': query,
	    'location': location,
	    'radius': radius,
	    'key': API_KEY
	}	
	
	# Request
	response = requests.get(endpoint_url, params = params)	
	# Results
	results = json.loads(response.content)	
	
	return results['results']
