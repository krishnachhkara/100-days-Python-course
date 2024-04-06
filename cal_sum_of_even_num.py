#calculate sum of even numbers from 1 to 100 using only one print statement
total = 0
for i in range(1,101):
    if(i % 2 == 0):
        total += i
print(f"The sum of all the even numbers between 1 and 100 is {total}")


#ma'ams way is shown below
total1 = 0
for num in range(2, 101, 2):
    total1 += num
print(total1)    