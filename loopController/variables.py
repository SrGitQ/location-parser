
class Place:
	def __init__(self, place:any):
		self.name:str = place['name']
		self.type:str = place['type']
		self.phone:str = place['phone']
		self.status:str = place['status']
		self.rating:str = place['rating']
		self.address:str = place['address']
		self.location:Location = Location(place['location'])
		self.visitorData:VisitorData = VisitorData(place['visitorData'])
		try:
			self.img:Img = Img(place['img'])
		except:
			self.img:Img = None
		try:
			self.busyDays:BusyDays = BusyDays(place['busyDays'])
		except:
			self.busyDays:BusyDays = None
		try:
			self.competency:list = [self.Place(p) for p in place['competency']]
		except:
			self.competency:list = None
		try:
			self.sentiment:Sentiement = Sentiement(place['sentiment'])
		except:
			self.sentiment:Sentiement = None
		try:
			self.busyHours:BusyHours = BusyHours(place['busyHours'])
		except:
			self.busyHours:BusyHours = None
		try:
			self.wordCloud:list = [WordCount(word) for word in place['wordCloud']]
		except:
			self.wordCloud:list = None
		try:
			self.reviews:list = place['reviews']
		except:
			self.reviews:list = None
	
	def data(self):
		return {
			'img':self.img.data(),
			'name':self.name,
			'type':self.type,
			'phone':self.phone,
			'status':self.status,
			'rating':self.rating,
			'location':self.location.data(),
			'address':self.address,
			'visitorData':self.visitorData.data(),
			'competency':self.competency,
			'busyDays':self.busyDays.data(),
			'sentiment':self.sentiment.data(),
			'wordCloud':[word.data() for word in self.wordCloud],
			'reviews':self.reviews,
			'busyHours':self.busyHours.data(),
		}

class Img:
	def __init__(self, src:str):
		self.src:str = src

	def data(self):
		return self.src

class Location:
	def __init__(self, location:dict):
		self.lat:float = location['lat']
		self.lng:float = location['lng']

	def data(self):
		return {
			'lat':self.lat,
			'lng':self.lng,
		}

class VisitorData:
	def __init__(self, visitorData:dict):
		self.url:str = visitorData['url']
	
	def data(self):
		return self.url

class DayTendency:
	def __init__(self, day:dict):
		self.day:str = day['day']
		self.people:int = day['people']
	
	def data(self):
		return {
			'day':self.day,
			'people':self.people,
		}

class BusyDays:
	def __init__(self, busyDays:dict):
		self.days:list = [DayTendency(day) for day in busyDays['days']]
	
	def data(self):
		return [day.data() for day in self.days]

class HoursTendency:
	def __init__(self, hour:dict):
		self.hour:str = hour['hour']
		self.people:int = hour['people']
	
	def data(self):
		return {
			'hour':self.hour,
			'people':self.people,
		}
	
class BusyHours:
	def __init__(self, busyHours:dict):
		self.hours:list = [HoursTendency(hour) for hour in busyHours['hours']]
	
	def data(self):
		return [hour.data() for hour in self.hours]

class WordCount:
	def __init__(self, word:dict):
		self.text:str = word['text']
		self.value:int = word['value']
	
	def data(self):
		return {
			'text':self.text,
			'value':self.value,
		}

class Sentiement:
	def __init__(self, sentiment:dict):
		self.positive:float = sentiment['positive']
		self.negative:float = sentiment['negative']
		self.neutral:float = sentiment['neutral']
	
	def data(self):
		return {
			'positive':self.positive,
			'negative':self.negative,
			'neutral':self.neutral,
		}
