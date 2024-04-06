#Wap to generate random password
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 
'k', 'l' ,'m' ,'n', 'o', 'p', 'q', 'r' ,'s' ,'t', 'u', 'v',
'w ','x', 'y', 'z','A' ,'B' ,'C', 'D' ,'E' ,'F' ,'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P' ,'Q' ,'R', 'S' ,'T', 'U' ,'V', 'W', 'X', 'Y', 'Z'  ]

num = ['0','1','2','3','4','5','6','7','8','9']
symbol =['!','@','#', '$','%','^','&','*','(' ,')', '_','+' ,'-']

print("Welcome to PyPassword  Generator")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_num = int(input("How many numbers would you like?\n"))

# #Easy level
# password = ""
# # for i in range(1,nr_letters+1):
#     # random_char = random.choice(letters)
#     # password += random_char
#     #above line combination is shown below
# for i in range(1,nr_letters+1):
#     password +=random.choice(letters)

# for i in range(1,nr_symbols+1):
#     password +=random.choice(symbol)    

# for i in range(1,nr_num+1):
#     password +=random.choice(numbers)

# print(password)    

#Hard level
password_list = []

for i in range(1,nr_letters+1):
    password_list.append(random.choice(letters)) #another method of adding elements

for i in range(1,nr_symbols+1):
    password_list +=random.choice(symbol)    

for i in range(1,nr_num+1):
    password_list +=random.choice(num)

print(password_list)#prints a list without shuffling

shuffle_list = random.shuffle(password_list)
# print(shuffle_list)#returns shuffled list

password1 = ""#list to string conversion starts
for char in password_list:
    password1 += char

print(f"{password1}")

