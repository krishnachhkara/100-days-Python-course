print("Welcome to love calculator ")
name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()
t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
e1 = name1.count("e")
total1 = t1+r1+u1+e1
t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
e2 = name2.count("e")
total2 = t2+r2+u2+e2
l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
y1 = name1.count("e")
love1 = l1+o1+v1+y1
l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
y2 = name2.count("e")
love2 = l2+o2+v2+y2

total = str(total1+total2)
love = str(love1+love2)
score1 = total+love
score = int(score1)
print(score)

if score<10 or score>90:
    print(f"Your score is {score},you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score},you are alright together.")
else:
    print(f"Your score is {score}, time to change the partner.")    


