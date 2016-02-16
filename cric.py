from bs4 import BeautifulSoup
import requests
import sqlite3
import time
import csv
import pymongo
from pymongo import MongoClient

class Scraper:
    """
    Do all the scraping and writing to the database using a scraper object.
    """
    def __init__(self):
        self.baseurl = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;page=%s;template=results;type=team;view=results"
	self.scrape_pages()	
 	
    def scrape_pages(self):
        """
        Loops through all the pages and grabs the results from them.
        """
        # Get the first page - there will always be a first page.
        index = 1
        self.getpage(index)
        # more_results returns True if that page contained results, false if it didn't.
        # This lets us know if we should continue to loop
        more_results = self.parse_page()
        while more_results:
            print "Scraping page %s" % index
            index += 1
            self.getpage(index)
            more_results = self.parse_page()
            # put a sleep in there so we don't hammer the cricinfo site too much
            time.sleep(1)

    def getpage(self, index):
        """
        Returns the HTML of a page of results, given the index.
        """
        page = requests.get(self.baseurl % index).text
        self.soup = BeautifulSoup(page)

    def parse_page(self):
        """
        Writes the contents of the page to the sqlite database.
        """
        for table in self.soup.findAll("table", class_ = "engineTable"):
            # There are a few table.engineTable in the page. We want the one that has the match
            # results caption
            if table.find("caption", text="Match results") is not None:
                rows = table.findAll("tr", class_ = "data1")
                for row in rows:
                    values = [i.text
                              for i in row.findAll("td")]
                    # if the only result in the table says "No records...", this means that we're
                    # at a table with no results. We've queried too many tables, so just return
                    # False
                    if values[0] == u'No records available to match this query':
                        return False

                    #self.cur.execute("""
                    #INSERT INTO results VALUES(
                    #?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    #)
                    #""", values)
		    
		    p = ({'team':values[0],'result':values[1],'margin':values[2],'toss':values[3],'bat':values[4],'blank':values[5],'opposition':values[6],'ground':values[7],'start_date':values[8],'blank2':values[9]})
		    
		    db.posts.insert(p)		
                #self.con.commit()
                # Return true to say that this page was parsed correctly
                return True

if __name__ == "__main__":
	client = MongoClient('localhost',27017)
	db = client.mydb
	
	scraper = Scraper()
