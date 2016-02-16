from __future__ import division
from bs4 import BeautifulSoup 
import requests
import csv
url = "http://www.espncricinfo.com/india/content/story/832513.html"
p = requests.get(url).text
s = BeautifulSoup(p)
a = s.find('table',{'class':'StoryengineTable'})
links = a.findAll('a')
#print links
rows = a.findAll('td')
dic = {}
for r in range(0,len(rows),3):
    yo= rows[r].findAll('a')
    for y in yo:
        hr = y['href']
        hr = hr.rstrip('.html')[-7:].lstrip('er/').lstrip('r/').lstrip('/')
        dic[hr] = r

g = open('basePrice.csv','w')
wr = csv.writer(g,dialect="excel")

with open('testpca.csv','r') as f:
    reader = csv.reader(f,dialect="excel")
    for row in reader:
        if row[0] != 'ID':
            playerid = row[0]
            print playerid            
            bp = dic[playerid] 
            vals = []
            vals.append(playerid)
            vals.append(rows[bp+2].text)
            wr.writerow(vals)
