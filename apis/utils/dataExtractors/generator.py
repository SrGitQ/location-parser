import requests
import json
from outscraper import ApiClient


def getDetailData(placeID):
	"""
	This function performs a concatennation of fields removing the unnecesary one from the 
	result of method api_client.google_maps_search and api_client.google_maps_reviews
	"""
	API_KEY = requests.get('http://localhost:5000/keys/OUTSCRAPPER_KEY').text
	api_client = ApiClient(api_key=API_KEY)

	generalData = api_client.google_maps_search(placeID,
	    language='es', 
	    fields=['about','reviews_per_score', 'verified','reviews'])

	generalData[0][0]['total_reviews'] = generalData[0][0].pop('reviews')

	timeData = api_client.google_maps_reviews(placeID,
	    language='es',
	    fields=['popular_times','reviews_data'])
	timeData[0].pop('reviews_data')
	resultDict = MergeDict(generalData[0][0], timeData[0])  

	return resultDict

def MergeDict(dict_1, dict_2):
	"""
	Function to combine two dictonaries previously processed from json format
	"""
	result = dict_1 | dict_2
	return result


def informationPlace(placeID):
    """
    Function to search a specific place given a query using place from places API
    """

    extraData = getDetailData(placeID)

    results = MergeDict(basicInformationPlace(placeID), extraData)

    return results


def basicInformationPlace(placeID):
	"""
	Function to search a specific place given a query using place from places API
	"""
	# Endpoint
	endpoint_url = 'https://maps.googleapis.com/maps/api/place/details/json'
	
	# API GOOGLE
	API_KEY = requests.get('http://localhost:5000/keys/GOOGLE_MAPS_KEY').text

	# Parameters
	params = {
		'place_id': placeID,
		'key': API_KEY,
		'language': 'es'
	}

	# Request
	response = requests.get(endpoint_url, params = params)

	# Results
	data = json.loads(response.content)

	return data['result']
