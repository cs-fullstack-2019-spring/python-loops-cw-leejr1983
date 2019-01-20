from _ast import If


def main():

    # problem1()
    #problem2()
    #problem3()
    problem4()



#     Exercise 1:
# Print -20 to and including 50.
# Use any loop you want.

def  problem1():
    for numbers in range(-20,51):
        print (numbers)

# Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.

def problem2():
    for numbers in range (0,21,2):
        print(numbers)

# Exercise 3:
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
# Ex.Output
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE

def problem3():
    userInput= int(input("Please enter number 1"))
    userInput2= int(input("Please enter number 2"))
    userInput3= int(input("please enter number 3"))
    average= int((userInput + userInput2 + userInput3) /3)
    print("The average of",str(userInput),str(userInput2),str(userInput3),"is",str(average))

# Exercise 4:
# Password Checker - Ask the user to enter a password. Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

def problem4():
    userInput= input("Please enter password")
    userInput2= input("Please verify your password")

    while (userInput2 != userInput or "q"):

        if (userInput == userInput2):
            print ("Thank you")
            break
        elif (userInput2 == "q"):
             print ("User has chosen to quit")
             break
        else:
            userInput2= input("Please verify your password")





















if __name__ == '__main__':
    main()