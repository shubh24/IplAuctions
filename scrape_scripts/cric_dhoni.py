from bs4 import BeautifulSoup
import requests
import sqlite3
import time
import csv
import pymongo
from pymongo import MongoClient

class Scraper:

    def __init__(self):
        self.baseurl = "http://www.espncricinfo.com/ci/content/player/28081.html"
	self.scrape_pages()	
 	
    def scrape_pages(self):

        index = 1
        self.getpage(index)
	self.parse_page()

	'''        
	while more_results:
            print "Scraping page %s" % index
            index += 1
            self.getpage(index)
            more_results = self.parse_page()
            # put a sleep in there so we don't hammer the cricinfo site too much
            time.sleep(1)
	'''
    def getpage(self, index):

        page = requests.get(self.baseurl).text
        self.soup = BeautifulSoup(page)

    def parse_page(self):

        for table in self.soup.findAll("table", class_ = "engineTable"):
   
		rows = table.findAll("tr", class_ = "data1")
		for row in rows:
		    values = [i.text
		              for i in row.findAll("td")]
		   
		    #if values[0] == u'No records available to match this query':
		    #    return False
		    print values
	    
		    p = ({'type':values[0],'matches':values[1],'inns':values[2],'no':values[3],'runs':values[4],'hs':values[5],'ave':values[6],'bf':values[7],'sr':values[8],'hundreds':values[9],'fiftys':values[10],'fours':values[11],'sixes':values[12],'ct':values[13],'st':values[14]})
		    
		    db.posts.insert(p)		
		break
        return True

if __name__ == "__main__":
	client = MongoClient('localhost',27017)
	db = client.dhoni1	
	scraper = Scraper()
