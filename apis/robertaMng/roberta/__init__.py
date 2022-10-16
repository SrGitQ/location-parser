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
