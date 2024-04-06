import random as r
a = r.randint(0,2)
print("Enter 0 for rock , 1 for paper , and 2 for scissors")

b = int (   input("enter your choice"))

# if (a==b):
#     print("Draw")
# if(a==0 and b ==2):
#     print( "You Lose!!")
# if(a==1 and b==0):
#     print("you lose")
# if(a==0 and b==1):
#     print("You win")
# if(a==1 and b==2):
#     print("ypu win")

if (b == 0 and a ==2 ):
    print("Computer choose",a)
    print("you win")
elif(a>b):
    print("Computer choose",a)
    print("you loose")
else:
    print("Computer choose",a)
    print("you loose")        