from operator import itemgetter
stocks=[
    {'tcker':'AAPL','price':200},
    {'tcker': 'GOOG', 'price': 201},
    {'tcker': 'NETFLEX', 'price': 240}

]
for x in sorted(stocks,key=itemgetter('tcker')):
    print(x)