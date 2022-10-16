from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import numpy as np

def countWords(reviews):
  try:
    res = [sub.split() for sub in reviews]
  except:
    return []
  
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
  try:
    top_10 = fdist.most_common(20)
  except:
    top_10 = fdist.most_common(10)
  
  data = [{'text':word[0], 'value':word[1]} for word in top_10]
  return data

def wordCounter(texts):
	texts_normalized = {}
	print(texts)
	for text in texts:
		t = text.lower()
		t = re.sub('(\.|\,|\"|\d+|\$|\?)','',t)
		t = re.sub('(\(|\))',' ',t)
		words = re.findall('\w+', t)
		for word in words:	
			if len(word) > 3:
				if word not in texts_normalized:
					texts_normalized[word] = 1
				else:
					texts_normalized[word] += 1
	dictionary_keys = list(texts_normalized.keys())[:15]
	sorted_dict = {dictionary_keys[i]: sorted(texts_normalized.values())[::-1][i] for i in range(len(dictionary_keys))}

	words_c = []
	for word in sorted_dict:
		words_c.append({'text':word, 'value':sorted_dict[word]})

	return words_c
