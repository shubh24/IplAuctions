from __future__ import division
from bs4 import BeautifulSoup 
import requests
import csv
import time
links = []
with open('ids.csv','r') as g:
    reader = csv.DictReader(g)
    for row in reader:
        links.append(row)
ids = []
for i in links:
    ids.append(i['IDS'])

f = open('matchBymatch2.csv','wb')
wr = csv.writer(f,dialect = 'excel')

for i in ids:
    try:
        #playerid = links[i]['href'].rstrip('.html')[-7:].lstrip('er/').lstrip('r/').lstrip('/')
        print i
        playerid = i
        newLink = 'http://stats.espncricinfo.com/ci/engine/player/' + playerid + '.html?class=3;template=results;type=batting;view=innings'
        p = requests.get(newLink).text
        s = BeautifulSoup(p)
        a = s.findAll('table',{'class':'engineTable'})
        if len(a) > 2:
            tableBatting = a[3]
            scores = []
            srs = []
            ris = []
            sris = []
            pris = []
            chis = []
            rows = tableBatting.findAll('tr')
            arrCount = 0
            vals = []
            for r in range(1,len(rows),1):
                print r
                c = rows[r].findAll('td')
                if len(c) > 1:
                    if (c[0].text[-1]) == '*':
                        notout = 1
                    else:
                        notout = 0
                    if c[0].text != 'TDNB' and c[0].text!='DNB':
                        vals.append(int(c[0].text.rstrip('*')))
            wr.writerow(vals)
            print playerid
    except:
        i -= 1
        print 'yolo'
        time.sleep(1)
        continue
