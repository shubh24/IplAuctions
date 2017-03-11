from bs4 import BeautifulSoup
import requests
import pymongo
import csv
from pymongo import MongoClient

class Scraper:

    def __init__(self,url,name,price):
        self.baseurl = url
	self.name = name
	self.price = price		
	self.scrape_pages()
	
 	
    def scrape_pages(self):

        pg = requests.get(self.baseurl).text
		self.sp = BeautifulSoup(pg)

		a = self.sp.find('table',{'id':'ipl-battingPerformance'})
		rows = a.findAll('tr')
		count = len(rows)
		counter = 0
		values = []
		for row in rows:
			counter += 1
			if counter == count:
				cols = row.findAll('td')
				for col in cols:
					if not (col.string) == None:
						if col.string == '-':
							values.append('0')
						else:
							values.append(col.string)
	
	p = ({'name':self.name,'matches':values[0],'inns':values[1],'no':values[2],'runs':values[3],'hs':values[4],'ave':values[5],'sr':values[6],'hundreds':values[7],'fiftys':values[8],'fours':values[9],'sixes':values[10],'ct':values[11],'price':self.price})
	print p	    
    	db.posts.insert(p)	
	
	

if __name__ == "__main__":
	client = MongoClient('localhost',27017)
	db = client.auction_batsmen2	
	with open('auction_data.csv','r') as fp:
		reader = csv.reader(fp,delimiter=',')
     		for row in reader:
			name = row[0]
			url = row[1]
			price = row[2]
			scraper = Scraper(url,name,price)
