# test values are 78 65 89 86 55 91 64 89 
#question code start
scores = input("input a list os scores of student : ").split()
for n in range(0,len(scores)):
    scores[n] = int(scores[n])
print(scores)  
#my code starts  
a = scores[0]
highest = 0
for i in scores:
    if(a>i):
        highest = a
    elif(i>a):
        a = i
        highest = a
print(f"The highest score in the class is {highest}")


#above is my code , now ma'am code is started below
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score)        
