from flask import Flask, send_from_directory;
from loopController.variables import Place;
from bson.json_util import dumps
from flask_cors import CORS, cross_origin
from flask import send_file
import requests
import img2pdf
from PIL import Image

from loopController.dataRequester import placeTransform,  getOneBusiness

data = {
	'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
	'name':'La reposteria de Osiris',
	'type':'Restaurant',
	'phone':'+51 999 140 5395',
	'status':'Closed',
  'place_id':'ChIJN1t_tDeuEmsRUsoyG83frY4',
	'rating':4.5,
	'location':{'lat':20.9863018, 'lng':-89.733405},
	'address':'3 North Trenton St. Burnsville, MN 55337',
	'visitorData':{'url':'www.google.com'},
	'competency':None,
	'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},
	'sentiment':{'positive':20, 'neutral': 20, 'negative': 30},
	'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],
	'reviews':[13, 10, 2, 3, 4],
	'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},
}
data1 = {
	'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
	'name':'Otra cosa',
	'type':'Restaurant',
	'phone':'+51 999 140 5395',
  'place_id':'ChIJN1t_tDeuEmsRUsoyG83frY4',
	'status':'Closed',
	'rating':4.5,
	'location':{'lat':20.9863018, 'lng':-89.733405},
	'address':'No tiene direccion',
	'visitorData':{'url':'www.google.com'},
	'competency':None,
	'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},
	'sentiment':{'positive':420, 'neutral': 20, 'negative': 30},
	'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],
	'reviews':[13, 10, 2, 3, 4],
	'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},
}
data2 = {
	'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
	'name':'Otra cosa 2',
	'type':'Restaurant',
	'phone':'+51 999 140 5395',
  'place_id':'ChIJN1t_tDeuEmsRUsoyG83frY4',
	'status':'Closed',
	'rating':4.5,
	'location':{'lat':20.9863018, 'lng':-89.733405},
	'address':'si tiene direccion',
	'visitorData':{'url':'www.google.com'},
	'competency':None,
	'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},
	'sentiment':{'positive':420, 'neutral': 20, 'negative': 30},
	'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],
	'reviews':[13, 10, 2, 3, 4],
	'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},
}

#place:Place = Place(data);
#place.competency = [Place(data), Place(data), Place(data), Place(data)]

places = None
current_search_place = None;

app = Flask(__name__);
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#The main route will return the current state of the app
@app.route('/')
@cross_origin()
def index():
	return current_search_place.data()

@app.route('/file/<path:path>')
def file(path):
  if path != 'fullpage.png':
    res = requests.get('http://localhost:4000/')
    image = Image.open('./loopController/static/fullpage.png')
    pdf_bytes = img2pdf.convert(image.filename)
    file = open('./loopController/static/dashboard.pdf', "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
  return send_file('./static/dashboard.pdf', as_attachment=True)#send_from_directory("./static/", path)

@app.route('/icons/<path:path>')
def icons(path):
  return send_from_directory("./static/icons/", path)

@app.route('/codes/<path:path>')
def codes(path):
  return send_from_directory("./static/codes/", path)

from loopController.dataRequester import OneBusinessMain, getOneBusinessStandar

import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient("mongodb+srv://karla:0101.0101@maps.yasmsoc.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client['mapsG']
collec = db['places']

from loopController.Qrgenerator import generateQRCode
from flask import redirect
@app.route('/place/<id>')
def set_place(id):
  global current_search_place
  #search in the database given the id
  data = collec.find_one({'place_id':id})
  if data:
    #if it is the database, return that data
    current_search_place = Place(data)
    return redirect("http://localhost:3000", code=302)
  else:
    #else, scrap the data process return and save it
    print('scraping... '+id)
    data = OneBusinessMain(id)
    print('scraped', data)
    current_search_place = placeTransform(data)
    requests.get(f'http://localhost:4000/img?url={current_search_place.data()["url"].split("=")[1]}&id={id}')
    collec.insert_one(current_search_place.data())
    if 'website' in data:
      generateQRCode(data['website'], id)
    return 'ok'


@app.route('/place')
def get_current_place():
  return current_search_place.data()

#get the places
@app.route('/places')
def places_sender():
  return [p.data() for p in places]

stack_places = []

@app.route('/compare/<id>')
def startComp(id):
  global stack_places
  if id not in stack_places:
    stack_places.append(id)
  print(stack_places)
  return 'ok'

pool_places = []
@app.route('/compare/reset')
def resetComp():
  global pool_places
  global stack_places
  global compare_status
  compare_status = False
  stack_places = []
  pool_places = []
  return 'ok'


import multiprocessing as mp

def MulpleBusinessMain(ids):
    pool_obj = mp.Pool(20)
    placesResults = pool_obj.map(OneBusinessMain,ids)
    return placesResults

from loopController.variables import BasicPlace
@app.route('/compare/scrape')
def scrapeComp():
  print('scraping...')
  global current_search_place
  for i, id in enumerate(stack_places):
    # check if the place is in the database
    data = collec.find_one({'place_id':id})
    if data:
      print('found in database')
      #if it is the database, return that data
      if i == 0:
        current_search_place = Place(data)
      else:
        pool_places.append(Place(data))
    else:
      print('not found in database')
      if i == 0:
        current_search_place = placeTransform(getOneBusiness(id))
      else:
        #search details for that place and save it
        print('scraping in google... '+id)
        prop = getOneBusinessStandar(id)
        #basic object
        pool_places.append(BasicPlace(prop))
  current_search_place.competency = pool_places
  print('scraped', current_search_place.data())
  return 'ok'
  


  return 'ok'
