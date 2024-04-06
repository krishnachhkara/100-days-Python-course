a = 5
b = 100
#method one
a = a + b
b = a - b
a = a - b
print(a)
print(b)

#method two using 3rd variable
c = a
a = b
b = c
print(a)
print(b)

#method three 
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)