#In this file we see diff fun operated on str


#in this file we are going to see different ways to write and edit name in python
name = input("Enter your name :").strip().title()
#we cancombine multiple fun like i have done above
# first way basic
print("hello",name)

"""second way in this f is useed for formating and
 the word in braces is variable name aur if give in inverted commas
 then considered as the value as shown"""
print(f"hello",{name})
print(f"hello",{"krishna"})
print(f"Hello {name}")#another way

# if we write f and not use braces the f is ignored
print(f"hello",name)


# third way using string concatenation method
greeting = "hello"
msg = "my friend"
print(greeting + " " + msg + ", " +  name )

#method to remove white spaces(means empty spaces) from the input
name = name.strip()
print(f"Hello {name}")

#capitalise function just capitalise first letter of the very first word
name = name.capitalize()
print(f"hello",{name})

#title fun is used to capitalise first letter of every word 
name = name.title()
print(f"hello,chick",{name})

#using mutlipe fun in single line
#in this way working of fun is from left to right
#for example
name = name.strip().title()
print(f"Hello {name}")