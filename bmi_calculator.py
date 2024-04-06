h = input("Enter your height in meters:  ")
w = input("Enter your weight in kilograms:  ")
bmi = float(w)//float(h)**2
if bmi<18.5:
    print("You are under weight")
elif bmi>18.5 and bmi<25:
    print("You have normal weight")
else:
    print("You are overweight")        
