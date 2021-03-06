import csv
with open('matchBymatch2.csv','rb') as f:
    reader = csv.reader(f,delimiter=',')
    master = []
    for row in reader:
        scores = []
        for i in range(0,len(row),1):
            if (row[i]==''):
                break            
            scores.append(row[i])
            i+=1        
        master.append(scores)
#print master
playerCAA = []
for row in master:
    sumOfDiff = 0
    aveSum = 0
    for i in range(0,len(row),1):
        aveSum += int(row[i])
        for j in range(0,len(row),1):
            sumOfDiff += abs(int(row[i])-int(row[j]))
    ave = float(aveSum)/len(row)
    
    if ave == 0:
        giniIndex = 1
    else:
        giniIndex = float(sumOfDiff/(2*ave*len(row)*len(row)))    
    caa = ave*(1-giniIndex)
    playerCAA.append(caa)
#print playerCAA


f = open('caa.csv','wb')
wr = csv.writer(f,dialect = 'excel')

for i in range(0,len(playerCAA),1):
    vals = []
    vals.append(playerCAA[i])    
    wr.writerow(vals)
    


'''
price = []
with open('mynew.csv','r') as fi:
    re = csv.reader(fi,delimiter=',')
    for row in re:
        price.append(int(row[0]))
print price
playerCAA = []
for row in master:
    sumOfDiff = 0
    aveSum = 0
    for i in range(0,len(row),1):
        aveSum += int(row[i])
        for j in range(0,len(row),1):
            sumOfDiff += abs(int(row[i])-int(row[j]))
    ave = float(aveSum)/len(row)

    giniIndex = float(sumOfDiff/(2*ave*len(row)*len(row)))    
    caa = ave*(1-giniIndex)
    playerCAA.append(caa)
print playerCAA
    
plt.scatter(price,playerCAA)

    plt.annotate(label,xy=(price,ave),ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()
'''
