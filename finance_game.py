# names = input("Enter the names of members separated by a comma ")
names = """krishna, chirag, vansh, vishal,tyagi"""
name = names.split(",")
# print(name)
import random
member = random.choice(name)
print(f"{member} will going to pay the bill")
