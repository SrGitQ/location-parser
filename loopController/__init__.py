from flask import Flask, send_from_directory;
from loopController.variables import Place;
from bson.json_util import dumps
from flask_cors import CORS, cross_origin
from flask import send_file
import requests
import img2pdf
from PIL import Image

data = {
	'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
	'name':'La reposteria de Osiris',
	'type':'Restaurant',
	'phone':'+51 999 140 5395',
	'status':'Closed',
	'rating':4.5,
	'location':{'lat':20.9863018, 'lng':-89.733405},
	'address':'3 North Trenton St. Burnsville, MN 55337',
	'visitorData':{'url':'www.google.com'},
	'competency':None,
	'busyDays': {'days':[{'day': 'M','people': 30,},{'day': 'T','people': 20,},{'day': 'W','people': 30,},{'day': 'T','people': 10,},{'day': 'F','people': 20,},{'day': 'S','people': 30,},{'day': 'S','people': 40}]},
	'sentiment':{'positive':420, 'neutral': 20, 'negative': 30},
	'wordCloud':[{'text': 'Manipulated', 'value': 80},{'text': 'told', 'value': 60},{'text': 'mistake', 'value': 11},{'text': 'thought', 'value': 30},{'text': 'bad', 'value': 17}],
	'reviews':[13, 10, 2, 3, 4],
	'busyHours': {'hours':[{'hour': '1','people': 10,},{'hour': '2','people': 20,},{'hour': '3','people': 30,},{'hour': '4','people': 30,},{'hour': '5','people': 50,},{'hour': '6','people': 60,},{'hour': '7','people': 20,},{'hour': '8','people': 10,},{'hour': '9','people': 70,},{'hour': '10','people': 100,},{'hour': '11','people': 10,},{'hour': '12','people': 20,},{'hour': '13','people': 30,},{'hour': '14','people': 50,},{'hour': '15','people': 50,},{'hour': '16','people': 60,},{'hour': '17','people': 70,},{'hour': '18','people': 20,},{'hour': '19','people': 58,},{'hour': '20','people': 40,},{'hour': '21','people': 10,},{'hour': '22','people': 20,},{'hour': '23','people': 30,},{'hour': '24','people': 40,}]},
}
data1 = {
	'img':{'src':'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
	'name':'Otra cosa',
	'type':'Restaurant',
	'phone':'+51 999 140 5395',
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

places = [Place(data), Place(data1), Place(data2)]
current_search_place = Place(data);

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

#modify the current place
@app.route('/place/<id>')
def set_place(id):
  global current_search_place 
  current_search_place = places[int(id)]
  return 'Data changed'

@app.route('/place')
def get_current_place():
  return current_search_place.data()

#get the places
@app.route('/places')
def places_sender():
  return [p.data() for p in places]