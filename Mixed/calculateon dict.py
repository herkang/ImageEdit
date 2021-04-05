
stocks={'AAPL':200,
    'GOOG': 201,
    'NETFLEX': 240}


min_price=min(zip (stocks.values(),stocks.keys()))
print(min_price)