# Champions Soccer Club Program - Output matches sample

players = {}

def display_menu():
    print("============================================================")
    print("**Welcome to Champions Soccer Club**")
    print("Please choose an option from the followings.")
    print("1) Add player name and score")
    print("2) Display all the player information and scores")
    print("3) Quit.")
    print("=============================================================")

def add_player():
    while True:
        # Get the players name
        name = input("Enter the player name : ").strip()
        if not name.isalpha():
            print("**Invalid name** The name should contain letters only. Please try again!")
            continue

        # Get the players score
        while True:
            score_input = input("Enter the score  : ").strip()
            if not score_input.isdigit():
                print("**Incorrect score** The score should be digits only. Please try again!")
                continue

            score = int(score_input)
            if score < 0 or score > 100:
                print("Page 2 of 3")
                print("**Incorrect score** The scores should be from 0-100. Please try again!")
            else:
                break  

        # Save players info
        players[name] = score

        # Ask to add another player
        repeat = input("Do you want to add another player? (Y/N) : ").strip().lower()
        if repeat not in ("y", "yes"):
            break

def display_players():
    if not players:
        print("No players added yet!")
        return

    print("Player & Score Details:")
    print("-------------------------------")
    print("Player")
    for name in players:
        print(name)
    print("Score")
    for score in players.values():
        print(score)
    print("-------------------------------")

# The main program loop
while True:
    display_menu()
    choice = input("Enter your choice : ").strip()

    if choice == "1":
        add_player()
    elif choice == "2":
        display_players()
    elif choice == "3":
        print("**GoodBye.. See you again!**")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")


