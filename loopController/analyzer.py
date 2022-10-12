from nltk.probability import FreqDist
from nltk.corpus import stopwords

#get the maximum dict in a list of dict given the percentage key
def get_max_dict(list_of_dict, key):
    return max(list_of_dict, key=lambda x: x[key])

def distribution(hours):
  aux_data = []
  for popular_t in hours:
    day = popular_t['day']
    #making the time variable given the dict structure 
    day = {'day':day, 'time':[]}
    for item in popular_t['popular_times']:
      try:
        hour = item['hour']
        percentage = item['percentage']
      except:
        pass
      day['time'].append({'hour':hour,'percentage':percentage})
    aux_data.append(day)
  
  aux_hours = {hour:0 for hour in range(1,25)}
  aux_days = {day:0 for day in range(1,8)}

  for day in aux_data:
    general = 0
    for hour in day['time']:
      time = hour['hour']
      percentage = hour['percentage']
      general += percentage
      if percentage > aux_hours[time]:
        aux_hours[time] = percentage
    aux_days[day['day']] = general
    

  parsed_hours = {'hours':[]}
  parsed_days = {'days':[]}
  for hour in aux_hours:
    parsed_hours['hours'].append({'hour':f'{hour}','people':aux_hours[hour]})
  days = {1:'M', 2:'T', 3:'W', 4:'T', 5:'F', 6:'S', 7:'S'}

  for day in aux_days:
    parsed_days['days'].append({'day':f'{days[day]}','people':aux_days[day]})

  return parsed_hours, parsed_days


def day_distribution(days):
  aux_data = []
  for popular_t in days:
    day = popular_t['day']
    #making the time variable given the dict structure 
    day = {'day':day, 'time':[]}
    for item in popular_t['popular_times']:
      try:
        hour = item['hour']
        percentage = item['percentage']
      except:
        pass
      day['time'].append({'hour':hour,'percentage':percentage})
    aux_data.append(day)

  aux_days = {day:0 for day in range(1,8)}

  for day in aux_data:
    general = 0
    #sum the percentage of each hour in a day
    hours = day['time']
    for hour in hours:
      general += hour['percentage']
    aux_days[day['day']] = general

  return aux_days

def countWords(reviews):
  res = [sub.split() for sub in reviews]
  
  #list of stopwords
  stopwords_list = stopwords.words("spanish")
  ##print(stopwords_list) 
  #create an empty list to store words
  words_no_punc = []
  resultList = sum(res, [])
  #iterate through the words list to remove punctuations
  for word in resultList:
    if word.isalpha():
      words_no_punc.append(word.lower())
  #create an empty list to store clean words
  clean_words = []
  #Iterate through the words_no_punc list and add non stopwords to the new clean_words list
  for word in words_no_punc:
    if word not in stopwords_list:
      clean_words.append(word)
  fdist = FreqDist(clean_words)
  top_10 = fdist.most_common(10)
  
  data = [{'text':word[0], 'weight':word[1]} for word in top_10]
  return data

# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('stopwords')
# print(countWords(samples[0]['reviews']))

