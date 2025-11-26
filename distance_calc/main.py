"""
ITP_A3_Task_1 Distance Calculator
"""
def show_results(speed, time):#Func to display results to user
    print(f"{'Minutes':^15} | {'Distance':^15}")
    print("-" * 33)
    for minute in range(1, time + 1):#For every minute calculate the distance and display it
        distance = speed * minute#Calculate the result
        print(f"{str(minute):^15} | {str(distance):^15}")#Print to user
def main():#Main function loop
    while True:
        try:
            speed=int(input("Enter the speed of the ball (in meters per minute): "))#Get user input for distance
            if not speed:#Check if there is input
                print("Please enter a value.")
                main()#Restart the loop
                break#Break current loop
            time=int(input("How many minutes has the ball travelled: "))#Get user input for time
            if not time:#Check if there is input
                print("Please enter a value.")
                main()#Restart the loop
                break#Break current loop
            assert speed >= 0#Check if input is a negative number
            assert time >= 0#Check if input is a negative number
            show_results(speed, time)#Send result
        except TypeError:#Check if wrong type
            print("Invalid Input: Please input a number.")
        except AssertionError:#Check for negative number
            print("Invalid Input: Please only enter positive numbers.")
        except ZeroDivisionError:#Check for Zero Division
            print("Error: Division by Zero is not allowed.")
if __name__ == "__main__":
    main()
