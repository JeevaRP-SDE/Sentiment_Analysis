import csv
import numpy as np
import nltk
from GoogleNews import GoogleNews
googlenews = GoogleNews()

with open('fortune.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 
 print("---------------------------------")
 for row in data:
  googlenews=GoogleNews(row['company'])
  googlenews=GoogleNews(lang='en')
  googlenews.get_news(row['company'])
  googlenews.search(row['company'])
  result = googlenews.page_at()
  googlenews.total_count()
  googlenews.result()
  a=googlenews.get_texts()
  print(row['company'])
  print("---------------------------------")
  print(a)
  print("---------------------------------")
  print(googlenews.total_count())
  print("---------------------------------")
  print(googlenews.result())
  print("---------------------------------")
  print(result)