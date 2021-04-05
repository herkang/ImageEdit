def myfunc(num):
  return num*2

x = map(myfunc, (1,2,3,4))

print(x)

#convert the map into a list, for readability:
print(list(x))