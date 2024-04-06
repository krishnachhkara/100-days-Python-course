print("""
        ______
       |     _|_
       |     |D1|
       |     | |
       |     | |                   
       |     | |     ___          
       |     | |    |   |         
      _|_____|_|_   | D2|         
     |  _______  |__|___|
     | |       | | 
     | |   D3  | |      
     | |_______| |     
     |     |     |     
     |  R1 |  R2 |     
     |     |     |   
     |_____|_____|   
""")
print("Welcome to the game of treasure hunting ")
door = input("Enter the door you want to open? D1 or D2 ")
if door == "D1":
   print("Entering the mansion ")
   print("You want to go back or open the door D3")
   decision = input("Back or Open? ")
   if decision.lower() == "back":
    print("You are going back to door D1 ")
   if decision.lower() == "open":
    print("Opening Door D3")
    room = input("Which room do you want to enter? Room 1 or Room2 ").lower()
    if room == "room1":
      print("You meet the beast ")
      print("Game Over")
    if room.lower() == "room2":
      print("congratulations")
      print("You found the chest with $1000")    
elif door == "D2":
    print("You fell in deep caverns.")
    print("Game Over")
else:
    print("Invalid choice")
