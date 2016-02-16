from __future__ import division
from bs4 import BeautifulSoup 
import requests
import csv
import time

#teams = ['csk','dd','kxip','kkr','mi','rr','rcb','srh']
year = '13'
teams = ['srh']
for team in teams:
    links = []
    f = open(str(team) + str(year)+'.csv','r')
    r = csv.reader(f)
    for row in r:
        links.append(row[0])

    g = open(str(team)+'Data' + str(year) + '.csv','wb')
    wr = csv.writer(g,dialect = 'excel')

    for i in range(0,len(links),1):
        try:
            print i    
            p = requests.get(links[i]).text
            s = BeautifulSoup(p)
            a = s.findAll('table',{'class':'engineTable'})
            if len(a) > 0:
                tableBatting = a[0]
                rows = tableBatting.findAll('tr')
                row = rows[len(rows)-1]
                cols = row.findAll('td')
                vals = []
                print cols[0],cols[6]            
                if cols[0].find('b').text == "Twenty20":
                    print 'hi'
                    vals.append(cols[6].text)
                    vals.append(cols[8].text)
                    vals.append(cols[9].text)
                    vals.append(cols[10].text)
                else:
                    print 'hoo'
                    for j in range(0,4,1):
                        vals.append(0)
                wr.writerow(vals) 
        except:
            i -= 1
            print 'yolo'
            time.sleep(1)
            continue
