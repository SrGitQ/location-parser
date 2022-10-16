from crypt import methods
from flask import Flask, request
import requests
from pymongo import MongoClient
import certifi
from bson.json_util import dumps
import json

#create the db
ca = certifi.where()

key = requests.get('http://localhost:5000/keys/MONGO_KEY').text
print(key)
client = MongoClient(key, tlsCAFile=ca)

db = client['mapsG']
collection = db['places']

app = Flask(__name__)


@app.route('/place', methods=['POST'])
def set_place():
	'''
		Insert a place in the database
	'''
	print(request.data, type(request.data))
	place = json.loads(request.data.decode('utf-8'))
	# place = json.loads(request.form['place'])

	if not place['place_id'] in collection.find():
		collection.insert_one(place)
		return 'ok'
	else:
		return 'The place is already in the database'



@app.route('/place/<id>')
def get_place(id):
    
	#search in the database given the id
	data = collection.find_one({'place_id':id})
	if data:
		#if it is the database, return that data
		return dumps(data)
	else:
		return 'not found', 404


if __name__ == '__main__':
	app.run(port=5001)
