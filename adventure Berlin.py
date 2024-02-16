description = "big room with chandelar hanging from the roof, and paintings all along the wall."
doors = ["north", "south", "west", "east"]

print ("hej och vökommen till Jimmys Berlin textäventyr")
print("********************************************")
print()

#main loop
run = True
while run:
    #print room
    print("You are standing in a " + description)
    print("There are doors to your:  ")
    
    #Format and print out all the directions that are available in the room.
    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    
    #print menu
    print("What do you want to do?")
    print("1. Go north")
    print("2. Go south")
    print("3. Go east")
    print("4. Go west")
    print("5. Look")
    print("0. Quit game")

    # Ask user for input
    choice = input("Please enter your choice: ")

    #sanitize user input
    if not choice.isnumeric():
        print("Sorry! Did not understand what you meant? Please give a number.")
        continue
    
    #Do something based on what the user asks for
    #if the user enters something you dont undestand, let him know
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print("you are going north")
    elif choice == 2:
        print("you are going south")
    elif choice == 3:
        print("you are going east")
    elif choice == 4:
        print("you are going west")
    elif choice == 5:
        print("you are looking really hard, but cant find anything new")
    else:
        print("Sorry, you asked for something I cannot do!")
