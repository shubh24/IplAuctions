from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient

class Scraper:

    def __init__(self):
        self.baseurl = "http://www.espncricinfo.com/ci/content/player/index.html?country=6"
	self.scrape_pages()	
 	
    def scrape_pages(self):

        pg = requests.get(self.baseurl).text
	self.sp = BeautifulSoup(pg)

	for table in self.sp.findAll("table", class_ = "playersTable"):
		rows = table.findAll("tr")
		for row in rows:
			cols = row.findAll("td",class_="divider")		
			for col in cols:
				#print col.get(
				for link in col.findAll("a"):
					url = "http://www.espncricinfo.com/" + link.get("href")		
					self.getpage(url)
					self.parse_page(link.contents[0])

    def getpage(self,url):

        page = requests.get(url).text
        self.soup = BeautifulSoup(page)	
	
    def parse_page(self,name):

        for table in self.soup.findAll("table", class_ = "engineTable"):
   
		rows = table.findAll("tr", class_ = "data1")
		for row in rows:
		    values = [i.text
		              for i in row.findAll("td")]
		   
		    #if values[0] == u'No records available to match this query':
		    #    return False
		    print values
	    
		    p = ({'name':name,'type':values[0],'matches':values[1],'inns':values[2],'no':values[3],'runs':values[4],'hs':values[5],'ave':values[6],'bf':values[7],'sr':values[8],'hundreds':values[9],'fiftys':values[10],'fours':values[11],'sixes':values[12],'ct':values[13],'st':values[14]})
		    
		    db.posts.insert(p)		
		break
        return True

if __name__ == "__main__":
	client = MongoClient('localhost',27017)
	db = client.india1	
	scraper = Scraper()
