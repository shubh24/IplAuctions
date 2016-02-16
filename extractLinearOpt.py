from bs4 import BeautifulSoup 
import requests
import csv
url = "http://www.espncricinfo.com/india/content/story/832513.html"
p = requests.get(url).text
s = BeautifulSoup(p)
a = s.find('table',{'class':'StoryengineTable'})
links = a.findAll('a')

f = open('linearOpt.csv','wb')
wr = csv.writer(f,dialect = 'excel')

for i in range(0,len(links),1):
    page = requests.get(links[i]['href']).text
    soup = BeautifulSoup(page)
    print soup
    tables = soup.findAll('table',{'class':'engineTable'})
    if len(tables) > 0:
		tableBatting = tables[0]
		rows = tableBatting.findAll('tr')
		lengthRows = len(rows)
		rowTwenty20 = rows[lengthRows-1]
		cols = rowTwenty20.findAll('td')
		vals = []
		vals.append(links[i].text)
		for c in cols:
		    vals.append(c.text)
		wr.writerow(vals)
		print links[i].text
