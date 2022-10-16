from utils.analyzer import wordCounter
from utils.analyzer.distribution import popular_times_analyzer
import requests

class Place:
	def __init__(self, place:any):
		self.name:str = place['name'] if 'name' in place else ''
		self.type:str = place['type'] if 'type' in place else ''
		self.place_id:str = place['place_id'] if 'place_id' in place else ''
		self.phone:str = place['formatted_phone_number'] if 'formatted_phone_number' in place else ''
		self.status:str = ('Open' if place['opening_hours']['open_now'] else 'Closed') if 'opening_hours' in place else ''
		self.url:str = (place['url']) if 'url' in place else ''
		self.website:str = (place['website']) if 'website' in place else ''
		self.rating:str = place['rating'] if 'rating' in place else ''
		self.address:str = place['formatted_address'] if 'formatted_address' in place else ''
		self.location = place['geometry']['location'] if 'geometry' in place else {}
		self.img:str = {'src':f'http://localhost:5000/static/imgs/{place["place_id"]}.png'} if 'place_id' in place else ''
		self.competency:list = place['competency'] if 'competency' in place else None

		if 'reviews' in place and len(place['reviews']) > 0:
			research = [p['text'] for p in place['reviews'] if 'text' in p]
			try:
				sentiments_reviews = [requests.post('http://localhost:5002', {'text':review}).json() for review in research]
				positive_avg = neutral_avg = negative_avg = 0
				for sentiment in sentiments_reviews:
					positive_avg += sentiment['positive']
					neutral_avg += sentiment['neutral']
					negative_avg += sentiment['negative']
				positive_avg /= len(sentiments_reviews)
				neutral_avg /= len(sentiments_reviews)
				negative_avg /= len(sentiments_reviews)
				self.sentiment = {'positive':positive_avg, 'neutral': neutral_avg, 'negative': negative_avg}
			except:
				self.sentiment = {'positive':0, 'neutral': 0, 'negative': 0}
			self.wordCloud:list = wordCounter(research)
		else:
			self.sentiment = {'positive':0, 'neutral': 0, 'negative': 0}
			self.wordCloud:list = []

		if 'popular_times' in place and place['popular_times'] != None:
			hours, days = popular_times_analyzer(place['popular_times'])
		else:
			hours, days = {'hours':[]},{'days':[]}

		self.busyDays:dict = days
		self.busyHours:dict = hours
		self.reviews:list = [place['reviews_per_score'][r] for r in place['reviews_per_score']] if 'reviews_per_score' in place else []
		self.ratings_total = place['user_ratings_total'] if 'user_ratings_total' in place else 0

	def generate(self):
		return {
			'name':self.name,
			'type':self.type,
			'place_id':self.place_id,
			'phone':self.phone,
			'website':self.website,
			'status':self.status,
			'url':self.url,
			'rating':self.rating,
			'address':self.address,
			'location':self.location,
			'img':self.img,
			'ratings_total':self.ratings_total,
			'busyDays':self.busyDays,
			'competency':self.competency,
			'sentiment':self.sentiment,
			'busyHours':self.busyHours,
			'wordCloud':self.wordCloud,
			'reviews':self.reviews
		}
