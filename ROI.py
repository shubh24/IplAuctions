import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient('localhost',27017)
db = client.auction_batsmen2
cur = db.posts.find()
aves = []
names = []
prices = []
for i in cur:
	aves.append(float(i['ave']))
	names.append(i['name'])
	prices.append(int(i['price']))

print aves,names,prices
plt.scatter(prices,aves)
for label,price,ave in zip(names,prices,aves):
	plt.annotate(label,xy=(price,ave),ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
plt.show()
