import heapq
grades=[32,45,67,89]
print(heapq.nsmallest(3,grades))
print(heapq.nlargest(2,grades))
stocks=[
    {'tcker':'AAPL','price':200},
    {'tcker': 'GOOG', 'price': 201},
    {'tcker': 'NETFLEX', 'price': 240}

]

print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))