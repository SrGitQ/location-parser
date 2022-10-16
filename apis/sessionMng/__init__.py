import requests
from flask import Flask, send_from_directory, send_file, request
from utils import QRGenerator
from flask_cors import CORS, cross_origin
from utils.keys import keys
import img2pdf
import json
from PIL import Image
from utils import Place
from utils.dataExtractors import nearbyTypeCollector, searchPlaces, informationPlace, basicInformationPlace

'''
	Create a flask server to attend the requests used the
	location parser, it gets petitions of series keys
'''

data = {'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},'name':'La reposteria de Osiris','type':'Restaurant','phone':'+51 999 140 5395','status':'Closed','place_id':'ChIJN1t_tDeuEmsRUsoyG83frY4','rating':4.5,'location':{'lat':20.9863018, 'lng':-89.733405},'address':'3 North Trenton St. Burnsville, MN 55337','visitorData':{'url':'www.google.com'},'competency':None,'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},'sentiment':{'positive':20, 'neutral': 20, 'negative': 30},'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],'reviews':[13, 10, 2, 3, 4],'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},}
data_2 = {'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},'name':'La reposteria de Osiris','type':'Restaurant','phone':'+51 999 140 5395','status':'Closed','place_id':'ChIJN1t_tDeuEmsRUsoyG83frY4','rating':4.5,'location':{'lat':20.9863018, 'lng':-89.733405},'address':'3 North Trenton St. Burnsville, MN 55337','visitorData':{'url':'www.google.com'},'competency':[data, data],'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},'sentiment':{'positive':20, 'neutral': 20, 'negative': 30},'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],'reviews':[13, 10, 2, 3, 4],'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#	General state is used to get the information in the frontend
#	general state manipulates a place object that has the usual information
#	and a list of places that are the competitors
place = data
competency = data_2


@app.route('/')
def hello_world():

	QRGenerator('https://www.google.com')

	return 'Hello, World!'


@app.route('/searchPlaces/<location>/<place>')
def searchPlacesText(location, place):
	return searchPlaces(place, location)


#	Maintain the current place to show in the dashboard
@app.route('/place')
@cross_origin()
def get_place():
	global place

	return place


#	Change the current place to show in the dashboard just for one place
@app.route('/place/<place_id>')
def set_place(place_id):
	#	if the place is the same as the current one, do nothing
	global place
	
	if place_id == place['place_id']:
		return 'The place is already set'

	#	Get the data from the database api
	data_from_db = requests.get('http://localhost:5001/place/'+place_id)

	# 	if there is the place in the database
	if data_from_db:
		place = data_from_db.json()
		return 'The place was set'

	else:#if the place is not in the database scrappe the data
		#	Scrappe the data and process the data
		place = Place(informationPlace(place_id)).generate()
		print(place)
		
		# get the image
		requests.get(f'http://localhost:4000/img?url={place["url"].split("=")[1]}&id={place_id}')
		
		# generate the QR
		if 'website' in place:
			QRGenerator(place['website'], place['place_id'])

		#	Insert the data in the database
		requests.post('http://localhost:5001/place', json=place)
		return place


#	Get the current competency to show in the dashboard
@app.route('/competency')
def get_competency():

	global competency

	return competency


#	Change the current competency to show in the dashboard
@app.route('/competency/q', methods=['POST'])
def set_competency():
	global place
	comp_ = json.loads(request.form['query'])
	print(comp_, type(comp_))

	comp_data = []
	# get the basic data from the types of places
	for type_ in comp_['types']:
		comp_data += nearbyTypeCollector(type_, comp_['location']['lat'], comp_['location']['lng'], comp_['radius'])
	#getting the data from detailed data
	data_comp = [basicInformationPlace(place['place_id']) for place in comp_data]

	data_comp = [Place(place).generate() for place in data_comp]

	if comp_['place_id'] == place['place_id']:
		return 'The competency is already set'
	
	db_info = requests.get('http://localhost:5001/place/'+comp_['place_id'])
	if db_info:
		# 
		comp_ = db_info.json()
		# extract and assign the competency places in competency field
		comp_['competency'] = data_comp
		# assign the competency to the global variable
		place = comp_
		print(place)
		return 'The competency was set'
	else:
		# extract the data from the place
		comp_ = Place(informationPlace(comp_['place_id'])).generate()
		# get the image
		requests.get(f'http://localhost:4000/img?url={comp_["url"].split("=")[1]}&id={comp_["place_id"]}')
		# generate the QR
		if 'website' in comp_:
			QRGenerator(comp_['website'], comp_['place_id'])
		# save in the database
		requests.post('http://localhost:5001/place', json=comp_)
		# extract and assign the competency places in competency field
		comp_['competency'] = data_comp
		# change the place global variable
		place = comp_
		print(place)
		return 'The competency was set'


@app.route('/icons/<path:path>')
def icons(path):
  return send_from_directory("./static/icons/", path)


@app.route('/codes/<path:path>')
def codes(path):
  return send_from_directory("./static/codes/", path)


@app.route('/file/<path:path>')
def file(path):
  if path != 'fullpage.png':
    res = requests.get('http://localhost:4000/')
    image = Image.open('./sessionMng/static/fullpage.png')
    pdf_bytes = img2pdf.convert(image.filename)
    file = open('./sessionMng/static/dashboard.pdf', "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
  return send_file('./static/dashboard.pdf', as_attachment=True)


@app.route('/keys/<key>')
def keyManager(key):
	'''
		Manage the keys used in the api
	'''

	return keys[key]

if __name__ == '__main__':
	app.run(port=5000)
