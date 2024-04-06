print("Welcome to KC's Pizza Store \n")
size = input("Enter the size of the pizza? S,M,L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
    price = 15
   
elif size == "M":
    price = 20
      
else:
    price = 25   

if add_pepperoni == "Y":
    if size == "S":
        price += 2    
    else:
        price += 3    

if extra_cheese == "Y":
        price += 1                

print(f"Your Final bill is: ${price}")        