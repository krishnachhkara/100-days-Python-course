print("Welcome to the tip calculator: ")
print("what was the total bill? ")
total_bill = float(input())
print("what percentage tip would you like to give? 10, 12 or 15?")
tip_percentage = int(input())/100
print("How many people to split the bill? ")
split_people = int(input())
# calculate the amount each person needs to pay
amount_each = (total_bill + (total_bill * tip_percentage)) / split_people
print("Each person should pay: $", format(amount_each, ".2f"))



