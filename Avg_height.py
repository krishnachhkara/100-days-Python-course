height = input("input a list of students heights : ").split()
for n in range(0,len(height)):
    height[n] = int(height[n])
print(height)    

#my code starts from here,but we can use sum func to sum all elements of list
#and len to calculate length of list
c = 0
a = 0
for i in height:
    c += 1
    a += i
print(a)
print(c)

avg_height = round(a/c)
print(avg_height)

 
