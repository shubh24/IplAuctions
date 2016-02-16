from __future__ import division
from bs4 import BeautifulSoup 
import requests
import csv

year = '11'
f = open('squads' + str(year) + '.csv','r')
re = csv.reader(f)
for j in re:
    team = j[0]
    url = j[1]

    p=requests.get(url).text
    s=BeautifulSoup(p)
    a = s.findAll('div',{'class':'large-13 medium-13 small-13 columns'})

    links = []
    for i in a:
        links.append('http://www.espncricinfo.com' + i.find('h3').find('a')['href'])


    g = open(str(team)+str(year)+'.csv','w')
    for i in links:
        g.write(i)
        g.write('\n')
