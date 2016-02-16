from __future__ import division
from bs4 import BeautifulSoup 
import requests
import csv
url = "http://www.espncricinfo.com/india/content/story/832513.html"
p = requests.get(url).text
s = BeautifulSoup(p)
a = s.find('table',{'class':'StoryengineTable'})
links = a.findAll('a')
import time


f = open('matchBymatch2.csv','wb')
wr = csv.writer(f,dialect = 'excel')

for i in range(94,len(links),1):
    try:
        playerid = links[i]['href'].rstrip('.html')[-7:].lstrip('er/').lstrip('r/').lstrip('/')
        print i    
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
            for r in range(1,len(rows),1):
                print r
                c = rows[r].findAll('td')
                if len(c) > 1:
                    if (c[0].text[-1]) == '*':
                        notout = 1
                    else:
                        notout = 0
                    if c[0].text != 'TDNB' and c[0].text!='DNB' and c[5].text != '' and c[5].text != '-':
                        scores.append(int(c[0].text.rstrip('*')))
                        srs.append(float(c[5].text))
                        position = int(c[6].text)
                        if position < 3:
                            pf = 0.5
                        else:
                            pf = position - 2
                        newerUrl = 'http://www.espncricinfo.com/' + c[13].find('a')['href']
                        page = requests.get(newerUrl).text
                        soup = BeautifulSoup(page)
                        battingInnings = soup.findAll('table',{'class':'batting-table innings'})
                        runSum = 0
                        srSum = 0    
                        counter = 0    
                        for b in battingInnings:
                            rowsMatch = b.findAll('tr')
                            for rowMatch in rowsMatch:
                                colsMatch = rowMatch.findAll('td')
                                if len(colsMatch) == 9:
                                    if (colsMatch[8].text != '' and colsMatch[8].text != '-'):
                                        runSum += int(colsMatch[3].text)
                                        srSum += float(colsMatch[8].text)
                                        counter += 1
                        if counter!=0:
                            meanRuns = runSum/counter
                            meanSR = srSum/counter
                            ris.append(scores[arrCount]/meanRuns)
                            sris.append(srs[arrCount]/meanSR)
                            pris.append(pf*scores[arrCount]/meanRuns)
                            chis.append(notout*scores[arrCount]/meanRuns)
                            arrCount+=1
            if len(ris)>0:        
                vals = []
                vals.append(playerid)
                
                vals.append(sum(ris)/len(ris))
                vals.append(sum(sris)/len(sris))    
                vals.append(sum(pris)/len(pris))        
                vals.append(sum(chis)/len(chis))
                
                wr.writerow(vals) 
                print playerid
    except:
        i -= 1
        print 'yolo'
        time.sleep(1)
        continue
