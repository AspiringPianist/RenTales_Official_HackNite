# pip install transformers torch ollama
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
class SceneAnalyze: # Analyzes the mood of a scene and rates it from 1 to 5, 1 being negative; 3 neutral; 5 positive
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    self.model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

  def analyze_sentiment(self,scene):
    tokens = self.tokenizer.encode(scene, return_tensors='pt')
    result = self.model(tokens)
    #print(result.logits)
    mood_int = (int(torch.argmax(result.logits))+1)
    mood = ''
    if(mood_int < 3):
      mood = 'negative'
    elif(mood_int ==3):
      mood = 'neutral'
    elif(mood_int>3):
      mood = 'positive'
    else:
      mood = 'neutral'
    return mood

# Get scene portion from the script
# Based on mood, select the music and populate the music list
# Give this info to reorganize.py who will queue music after every label
