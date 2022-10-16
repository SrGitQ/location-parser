import requests
import json

def searchPlaces(name, reference):
	API_KEY = requests.get('http://localhost:5000/keys/GOOGLE_MAPS_KEY').text

	# Endpoint
	endpoint_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

	# Parameters
	params = {
	    'query': name+reference,
	    'key': API_KEY
	}

	# Request
	response = requests.get(endpoint_url, params = params)
	# Results
	results = json.loads(response.content)
	
	return results['results']
