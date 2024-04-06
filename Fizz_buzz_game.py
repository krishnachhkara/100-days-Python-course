#Wap in which you print fizz when num divisible 3 occurs
# you print buzz  when the number is divisible by 5.
# if a number is divisible by both 3 and 5 then print FizzBuzz

#my code starts
for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0): 
        print("FizzBuzz")   
    elif(i % 3 == 0 ):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)