import time, json, os

running = True

# Have it write to a json file because if it doesn't, then it won't save.

# Use the Omar Bot as an example because I used json a lot in there.

os.chdir(r"C:\Users\OmarT\git_stuff\coordinate_keeper")

while running:
    with open('cords.json', 'r') as f:
        locations = json.load(f)
    r = False
    print("\n")
    choice = input("Add, read, or specify? (choose one): ").lower().strip()
    if choice == "add":
        choice = input("What is the location name? : ")
        if not f'{choice}' in locations:
            locations[f'{choice.strip().lower()}'] = {}
        cords = input("What are the coordinates of this location?: ")
        locations[f'{choice}'] = cords
        with open('cords.json', 'w') as f:
            json.dump(locations, f)
    elif choice == "read":
        print(locations)
    elif choice == "search":
        choice = input("What location would you like to see if you have?: ")
        if choice.strip().lower() in locations:
            print(f'{choice.strip().lower()} : {locations[choice.strip().lower()]}')
        else:
            print("This location doesn't exist.")
    elif choice == "quit":
        running = False
        exit()
    else:
        print("Not a valid option, try again.")
        r = True
    if not r:
        print("\n")
        choice = input("Quit? (y/n): ").lower().strip()
        if choice == "y" or choice == "yes":
            running = False
            exit()
