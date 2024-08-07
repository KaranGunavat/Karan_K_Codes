#Snake, Water, Gun Game. It is same as Rock, Paper, Scissors game
import random

# Mapping choices to numbers
'''
1 for snake
-1 for water
0 for gun
'''

# Computer randomly selects between 1, 0, and -1
computer = random.choice([1, 0, -1])

# User input
youStr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Dictionary to convert user input to corresponding numbers
# s = snake, w = water, g = Gun
youDict = {"s": 1, "w": -1, "g": 0}

# Dictionary to convert numbers back to readable choices
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Convert user's choice to the corresponding number
you = youDict[youStr]

# Display choices
print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

# Check for a draw
if computer == you:
    print("It's a Draw")
else:
    # Check all possible win/lose conditions
    if computer == -1 and you == 1:
        print("You Win!")  # Snake drinks water

    elif computer == -1 and you == 0:
        print("You Lose!")  # Water rusts gun

    elif computer == 1 and you == -1:
        print("You Lose!")  # Snake drinks water

    elif computer == 1 and you == 0:
        print("You Lose!")  # Gun shoots snake

    elif computer == 0 and you == -1:
        print("You Lose!")  # Water rusts gun

    elif computer == 0 and you == 1:
        print("You Win!")  # Gun shoots snake

    else:
        print("Something went wrong")# If user give invalid input
