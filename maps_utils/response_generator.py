#Funciones 
import re


def locationParser(locationstr:str)->list:
    return [float(point.replace(' ', '')) for point in locationstr.split(',')]

def getLocation(location:str)->str:
    try:
        lon, lat = locationParser(location)
        return f"point:{lat},{lon}"
    except:
        return location

def getRadius(rd:str)->str:
    return re.match('\d+', rd).group(0)

def nearbyPlaceInfo(data):
	try:	
		name = data['name']
	except:
		name = ''
	try:	
		location = [data['geometry']['location']['lat'],data['geometry']['location']['lng']]
	except:
		location = [0,0]
	try:	
		place_id = data['place_id']
	except:
		place_id = ''
	try:	
		business_status = data['business_status']
	except:
		business_status = ''
	try:	
		types = data['types']
	except:
		types = []
	try:	
		vicinity = data['vicinity']
	except:
		vicinity = ''
	try:	
		price_level = data['price_level']
	except:
		price_level = 0
	try:	
		rating = data['rating']
	except:
		rating = 0
	try:	
		user_ratings_total =  data['user_ratings_total']
	except:
		user_ratings_total = 0
	return {
		'name': name,
		'location': location,
		'place_id': place_id,
		'business_status': business_status,
		'types': types,
		'vicinity': vicinity,
		'price_level': price_level,
		'rating': rating,
		'user_ratings_total': user_ratings_total
	}
    
def searchNearbyPlace(place:any):
    #si lat lng no existe
        # obtenemos lat lng
    #obtener nearby places
    1

def searchPlace(place:any):
    # name y zone/address/lat lng
    # si lat lng existe
        # find place
        #obtenemos el place_id y lo guardamos
    # no lat lng existe
        #obtener lat lon a traves de geocoding
        # find place
        #obtenemos el place_id y lo guardamos
    
    # obtener place_details con el place_id
    1


def getPlaceData(data):
	try:
		name =  data['name']
	except:
		name = ''
	try:
		opening_hours =  data['opening_hours']
	except:
		opening_hours = {}
	try:
		address_components = data['address_components']
	except:
		address_components = []
	try:
		location =  [data['geometry']['location']['lat'],data['geometry']['location']['lng']]
	except:
		location = []
	try:
		business_status = data['business_status']
	except:
		business_status = ''
	try:
		formatted_address =  data['formatted_address']
	except:
		formatted_address = ''
	try:
		formatted_phone_number =  data['formatted_phone_number']
	except:
		formatted_phone_number = ''
	try:
		photos = data['photos']
	except:
		photos = []
	try:
		place_id =  data['place_id']
	except:
		place_id = ''
	try:
		rating =  data['rating']
	except:
		rating = 0
	try:
		reviews = data['reviews']
	except:
		reviews = []
	try:
		types =  data['types']
	except:
		types = []
	try:
		url =  data['url']
	except:
		url = ''
	try:
		website =  data['website']
	except:
		website = ''
	try:
		user_ratings_total =  data['user_ratings_total']
	except:
		user_ratings_total = 0
	return {
    	'name':name,
    	'opening_hours':opening_hours,
    	"address_components":address_components,
    	'location':location,
    	'business_status':business_status,
    	'formatted_address':formatted_address,
    	'formatted_phone_number':formatted_phone_number,
    	"photos":photos,
    	"place_id":place_id,
    	"rating":rating,
    	"reviews":reviews,
    	"types":types,
    	"url":url,
    	"website":website,
    	"user_ratings_total":user_ratings_total
	}


    

