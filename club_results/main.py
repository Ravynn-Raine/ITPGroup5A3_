score_dict = {}

def retrieve_scores():
    try:
        for player, score in score_dict.items(): # itterate over items in score dict
            yield player, score # return them one by one
    except Exception as e:
        print(f"An Error Occoured: {e}")

def add_player():
    try:
        while True: #Player name loop & validility
            player_name = input("Enter The Players Full Name: ") #Retrieve Input
            if all(char.isalpha() or char.isspace() for char in player_name) and player_name.strip(): #Validate Input
                break
            else:
                 print("Please enter a valid player's name.")
        while True: #Player score loop & validility
            player_score = input("Enter a players score: ") #Retrieve Input
            if player_score and player_score.isdigit(): #Validate Input
                player_score = int(player_score) #Convert Input
                if player_score <= 100 and player_score >= 1:#Validate again
                    break
                else:
                    print("Please enter a valid score between 1-100")
            else:
                print("Please enter a valid score")
        score_dict[player_name] = player_score #Add to dict "PlayerName:PlayerScore"
        while True: # Loop for checking for another player
            new_player = input("Do you want to add another player? (y/n) ")
            if new_player.lower() == "y" or new_player.lower() == "yes":
                return add_player()
            elif new_player.lower() == "n" or new_player.lower() == "no":
                return
            else:
                print("Please enter a valid option. (yes, no, y, n)")
    except Exception as e:
        print(f"An Error Occoured: {e}")

def main():
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

if __name__ == "__main__":
    main()
