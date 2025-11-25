"""
ITP_A3_Task_1

"""
try:
    d=int(input("Enter distance in km (km):  "))
    t=int(input("Enter time in minutes (m):  "))
    s=d/t
    print('Speed = {:.2f} km per minute'.format(s))

except TypeError:
    if d<0 or t<0:
        print("Invalid Input: Please only enter positive numbers above 0. ")
      
except ValueError:
    if d is not int or t is not int:
        print("Invalid Input: Please enter whole numeric values only. ")
        
except ZeroDivisionError:
    if d==0 or t==0:
        print("Error: Division by Zero not allowed.")
