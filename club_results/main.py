score_dict = {}

def retrieve_scores():
    print("Working on this")

def add_player():
    try:
        #Player's name loop & validility
        while True:
            player_name = input("Enter The Players Full Name: ")
            if all(char.isalpha() or char.isspace() for char in player_name) and player_name.strip():
                break
            else:
                 print("Please enter a valid player's name.")

        #Player's score loop & validility
        while True:
            player_score = input("Enter a players score: ")
            if player_score and player_score.isdigit():
                player_score = int(player_score)
                if player_score <= 100 and player_score >= 1:
                    break
                else:
                    print("Please enter a valid score between 1-100")
            else:
                print("Please enter a valid score")

        score_dict[player_name] = player_score

        new_player = input("Do you want to add another player? (Y/N)")
        if new_player.lower() == "y" or new_player.lower() == "yes":
            return add_player()
        elif new_player.lower() == "n" or new_player.lower() == "no":
            return
        return print(f"Added {player_name}")
    except Exception as e:
        print(f"An Error Occoured: {e}")

def main():
    while True:
        print("=======")
        print("(1) Add Player")
        print("(2)")
        print("(q) Quit")
        print("=======")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_player()
        elif choice == "2":
            retrieve_scores()
        elif choice.lower() == "q":
            print("Goodbye")
            break
        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()
