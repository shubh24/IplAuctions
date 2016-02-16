import csv

a = open('teamsVariance11.csv','r')
b= open('teamsVariance12.csv','r')
c = open('teamsVariance13.csv','r')
d = open('teamsVariance14.csv','r')
e = open('teamsVariance15.csv','r')

v = csv.reader(a)
w = csv.reader(b)
x = csv.reader(c)
y = csv.reader(d)
z = csv.reader(e)

arr = {}
brr = {}
crr = {}
drr = {}
err = {}

for i in v:
    print i[1]
    arr[i[0]]=pow(float(i[1]),0.5)
arr = sorted(arr.items(),key=lambda x:x[0])

for i in w:
    brr[i[0]]=float(pow(float(i[1])),0.5)
brr = sorted(brr.items(),key=lambda x:x[0])

for i in x:
    crr[i[0]]=float(pow(float(i[1]),0.5))
crr = sorted(crr.items(),key=lambda x:x[0])

for i in y:
    drr[i[0]]=float(pow(float(i[1])),0.5)

drr = sorted(drr.items(),key=lambda x:x[0])

for i in z:
    err[i[0]]=float(pow(float(i[1])),0.5)
err = sorted(err.items(),key=lambda x:x[0])

csk = []
dd = []
kkr = []
kxip = []
mi = []
rcb = []
rr = []

csk.append(arr[0][1])    
csk.append(brr[0][1])    
csk.append(crr[0][1])    
csk.append(drr[0][1])    
csk.append(err[0][1])    

dd.append(arr[1][1])
dd.append(brr[1][1])
dd.append(crr[1][1])
dd.append(drr[1][1])
dd.append(err[1][1])

kkr.append(arr[2][1])
kkr.append(brr[2][1])
kkr.append(crr[2][1])
kkr.append(drr[2][1])
kkr.append(err[2][1])

kxip.append(arr[3][1])
kxip.append(brr[3][1])
kxip.append(crr[3][1])
kxip.append(drr[3][1])
kxip.append(err[3][1])

mi.append(arr[4][1])
mi.append(brr[4][1])
mi.append(crr[4][1])
mi.append(drr[4][1])
mi.append(err[4][1])

rcb.append(arr[5][1])
rcb.append(brr[5][1])
rcb.append(crr[5][1])
rcb.append(drr[5][1])
rcb.append(err[5][1])

rr.append(arr[6][1])
rr.append(brr[6][1])
rr.append(crr[6][1])
rr.append(drr[6][1])
rr.append(err[6][1])

import matplotlib.pyplot as plt
import numpy as np
xticks = np.arange(2011, 2016, 1)

years = [2011,2012,2013,2014,2015]
p, = plt.plot(years,csk,label="CSK")
p, = plt.plot(years,dd,label="DD")
p, = plt.plot(years,kkr,label="KKR")
p, = plt.plot(years,kxip,label="KXIP")
p, = plt.plot(years,mi,label="MI")
p, = plt.plot(years,rcb,label="RCB")
p, = plt.plot(years,rr,label="RR")
plt.ticklabel_format(useOffset=False)
plt.xticks(xticks)
plt.legend(loc="upper center",ncol=4,fancybox=True,shadow=True)
plt.xlabel('Years')
plt.ylabel('Variance amongst batsmen')

plt.show()

