import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
#parse to object
y=json.loads(x)
print(y)
print(y["age"])
#convert from python object to JSON// json.dumps
print("---------")
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y=json.dumps(x)
print(y)