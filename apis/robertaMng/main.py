from flask import Flask, request
from scipy.special import softmax
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import AutoConfig


def Roberta():
	roberta_ML = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
	tokenizer = AutoTokenizer.from_pretrained(roberta_ML)
	config = AutoConfig.from_pretrained(roberta_ML)
	model = AutoModelForSequenceClassification.from_pretrained(roberta_ML)
	model.save_pretrained(roberta_ML)
	
	return tokenizer,model


tokenizer, model = Roberta()

def SentimentAnalyzer(review):

  encoded_input = tokenizer(review, return_tensors='pt')
  output = model(**encoded_input)

  scores = output[0][0].detach().numpy()
  scores = softmax(scores)

  return {'negative':float(scores[0]),'neutral':float(scores[1]),'positive':float(scores[2])}

app = Flask(__name__)

@app.route('/', methods=['POST'])
def Roberta():
	'''
		This is a API that takes text from the query
		and returns the porcentage of the text that is
		positive, negative or neutral
	'''
	text = request.form['text']
	rb = SentimentAnalyzer(text)
	print(rb)
	return rb

if __name__ == '__main__':
	# app.debug = True
	app.run(port=5002)
