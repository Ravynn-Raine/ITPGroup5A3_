import json
import os

score_dict = {}

def save_scores():#save score func
    with open("data.json", "w") as f:
        json.dump(score_dict, f, indent=4)

def load_scores():#load score func
    with open("data.json", "r") as f:
        loaded = json.load(f)
    score_dict.update(loaded)

def validate_score(score: str) -> bool:#check if score is valid
    if score.isdigit() and 1 <= int(score) <= 100:
        return True
    else:
        return False

def validate_name(name: str) -> bool:#check if name is valid
    if all(char.isalpha() or char.isspace() for char in name) and name.strip() and len(name) > 5:
        return True
    else:
        return False

def retrieve_scores():#retrieve and return scores
    try:
        for player, score in score_dict.items(): # itterate over items in score dict
            yield player, score # return them one by one
    except Exception as e:
        print(f"An Error Occoured: {e}")

def add_player():#add player to dict
    try:
        while True: #Player name loop & validility
            player_name = input("Enter The Players Full Name: ") #Retrieve Input
            if validate_name(player_name): #Validate Input
                break
            else:
                 print("Please enter a valid player's name.")
        while True: #Player score loop & validility
            player_score = input("Enter a players score: ") #Retrieve Input
            if validate_score(player_score): #Validate Input
                break
            else:
                print("Please enter a valid score")
        score_dict[player_name] = player_score #Add to dict "PlayerName:PlayerScore"
    except Exception as e:
        print(f"An Error Occoured: {e}")
    finally:
        while True: #Return or add another player loop
            new_player = input("Do you want to add another player? (y/n) ")
            if new_player.lower() == "y" or new_player.lower() == "yes":
                return add_player()#Start main loop
            elif new_player.lower() == "n" or new_player.lower() == "no":
                save_scores()
                return #Return to main menu
            else:
                print("Please enter a valid option. (yes, no, y, n) ")
def main():#main loop for UI
    while True:
        print("=======")
        print("(1) Add Player")
        print("(2) Display Player")
        print("(q) Quit")
        print("=======")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_player()
        elif choice == "2":
            print("Player's Name | Player's Score")
            for player,score in retrieve_scores(): # display the values returned
                print(f"{player} | {score}") # you will need to fix the display just here for testing
        elif choice.lower() == "q":
            print("Goodbye")
            break
        else:
            print("Please enter a valid option")

if __name__ == "__main__":#startup checks and init
    if os.path.exists("data.json"): #check if file exists
        load_scores()
    else:
        with open("data.json", "a"):# if it doesnt create it
            pass
    main()
