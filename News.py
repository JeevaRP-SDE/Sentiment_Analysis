import csv
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
  result = googlenews.page_at(2)
  googlenews.total_count()
  googlenews.results()
  googlenews.get_texts()
  print(googlenews.get_texts())
  print(row['company'])