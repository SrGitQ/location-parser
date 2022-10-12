import numpy as np
import requests
import json
import re
from outscraper import ApiClient
import multiprocessing as mp

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

from transformers import AutoConfig

import plotly.offline as pyo
import plotly.graph_objs as go

def MergeDict(dict_1, dict_2):
	"""
	Function to combine two dictonaries previously processed from json format
	"""
	result = dict_1 | dict_2
	return result


def dictValuesTransformation(dataDict):

    """
    This function returns a dict with the correct format 
    """

    for field in list(dataDict.keys()):
        if field == "geometry":
            dataDict['location'] = {'lat': dataDict['geometry']['location']['lat'],'lng':dataDict['geometry']['location']['lng']}
            dataDict.pop(field)
        if field == "reviews":
            comments = []
            for rev in dataDict['reviews']:
                comments.append(rev['text'])
            dataDict['reviews'] = comments
        if field == 'photos':
            photos_links = []
            for comp in dataDict['photos']:
                if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', comp['html_attributions'][0])[0] not in photos_links:
                    photos_links.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                                            comp['html_attributions'][0])[0])
            dataDict['photos'] = photos_links

    return dataDict


def removeFields(dataDict):
    """
    This function removes all fields that are not necessary for proccesing
    """

    NoFields = []
    Fields = ['business_status', 'formatted_address', 'formatted_phone_number', 'icon', 'icon_background_color', 'name', 'opening_hours', 'photos', 'place_id', 'rating', 'reviews', 'types', 'url', 'user_ratings_total', 'website', 'geometry','about','reviews_per_score','verified','popular_times','total_reviews']
    
    for field in dataDict:
        if field not in Fields:
            NoFields.append(field)

    for fieldx in NoFields:
        dataDict.pop(fieldx)
            
    return dataDict


def getDetailData(placeID):
    """
    This function performs a concatennation of fields removing the unnecesary one from the 
    result of method api_client.google_maps_search and api_client.google_maps_reviews
    """

    api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTU5NzIyNzM2OTAzODU0NDAxNTB8NzU5ZTJkZGU5Yg')

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


def getOneBusiness(placeID):
    """
    Function to search a specific place given a query using place from places API
    """
    # Endpoint
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    
    # API GOOGLE
    API_KEY='AIzaSyCFXJsJDyC32kIJ2AHu2IMF1-osa6uKwSo'

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

    extraData = getDetailData(placeID)

    results = MergeDict(data['result'], extraData)

    return results


def getMultipleBusiness(query,lat,lon,radius):
  """
  Function to search places given a query using text_search from places API
  """
  # Position
  location = f'{lat},{lon}'

  # API GOOGLE
  API_KEY='AIzaSyCFXJsJDyC32kIJ2AHu2IMF1-osa6uKwSo'
  
  # Endpoint
  endpoint_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

  # Parameters
  params = {
      'query': query,
      'location': location,
      'radius': radius,
      'key': API_KEY
  }

  # Request
  response = requests.get(endpoint_url, params = params)

  # Results
  results = json.loads(response.content)

  
  return results['results']


def OneBusinessMain(placeID):
    """
    This function receives a place id and delivers the structured information of one business 
    place by calling other functions inside previously defined
    """

    OneBusiness = getOneBusiness(placeID)
    
    OneBusiness = removeFields(OneBusiness)

    OneBusiness = dictValuesTransformation(OneBusiness)

    return OneBusiness


def MulpleBusinessMain(query,lat,lon,radius):
    """
    This function takes a query, a coordinate and a radius to deliver a set of places(20)
    which are processed using 20 threads to optimize the output result.
    """

    MBdict = getMultipleBusiness(query,lat,lon,radius)

    pool_obj = mp.Pool(20)

    places = [place['place_id'] for place in MBdict]

    placesResults = pool_obj.map(OneBusinessMain,places)

    return placesResults
  
from loopController.analyzer import countWords, distribution
from loopController.variables import Place

def placeTransform(data):
  if data['popular_times'] != None:
    hours, days = distribution(data['popular_times'])
  else:
    hours, days = {'hours':[]},{'days':[]}
  
  if 'opening_hours' in data:
    status = 'Open' if data['opening_hours']['open_now'] else 'Closed'
  else:
    status = ''
  
  if 'formatted_phone_number' in data:
    phone = data['formatted_phone_number']
  else:
    phone = ''
  
  if 'website' in data:
    website = data['website']
  else:
    website = ''
  
  if 'reviews' in data:
    words = countWords(data['reviews'])
  else:
    words = []
  print('from data request: ', data, words)
  return Place({
	  'img':{'src':f'http://localhost:5000/static/imgs/{data["place_id"]}.png'},
    'place_id': data['place_id'],
	  'name':data['name'],
	  'type':data['types'][0],
    'url':data['url'],
	  'phone':phone,
	  'status':status,
	  'rating':data['rating'],
	  'location':data['location'],
	  'address':data['formatted_address'],
	  'visitorData':{'url':website},
	  'busyDays': days,
	  'sentiment':{'positive':420, 'neutral': 20, 'negative': 30},
	  'wordCloud':words,
	  'reviews':[data['reviews_per_score'][r] for r in data['reviews_per_score']],
	  'busyHours': hours
  })







