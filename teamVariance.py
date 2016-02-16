import csv
import numpy as np

#teams = ['csk','dd','kxip','kkr','mi','rr','rcb']
year = '13'
teams = ['csk']
g = open('teamsVariance_csk13'+str(year)+'.csv','w')
wr = csv.writer(g)
vals = []

for team in teams:
    with open(str(team)+'Data' + str(year) + '.csv','r') as f:
        reader = csv.reader(f)
        for i in reader:
            if i[0]=='-':
                i[0]=0
            if i[1]=='-':
                i[1]= 0
            if i[2]=='-':
                i[2]= 0
            if i[3]=='-':
                i[3]= 0
            vals.append(0.5*pow(float(i[0]),2) + 0.5*pow(float(i[1]),1.5) + 0.8*int(i[2]) + 0.3*int(i[3]))
            
    variance = np.var(vals)
    mean = np.mean(vals)
    wr.writerow((team,variance,mean))


