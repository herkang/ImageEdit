from struct import *
#store as bytes data
packed_data=pack('iif',6,19,4.73)
print(packed_data)
#how many bytes requred to send data
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
#to get back to normal
original=unpack("iif",b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
print(original)
