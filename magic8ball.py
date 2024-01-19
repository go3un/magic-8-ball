# Ella Kim
# 1/19/24
# Magic 8 Ball

# Initialize
import random

# Possible responses
responseList = ["You wish.", "For sure!", "Duh.", "That's not...",
                "YES!!", "Sorry, no.", "Maybe?", "What do you think.",
                "You can count on it!", "Possibly..", "That's not a question for me.", 
                "Ur funny", "OFC", "Yeah I guess", "Yes", "No"]

# Functions
# Randomizes and prints your answer from the Magic 8 Ball
def randomize():
    print(random.choice(responseList))

# Takes input on whether the user wants to ask another question or exit
def takeInput():
    player_input = input("Would you like to... \n (Yes) Ask another question \n (No) Exit the program") 
    if player_input == "Yes":
        start()
    elif player_input == "No":
        quit()

# Starts the program by asking for a question, makes sure it ends with a question mark, and loops
def start():
    x = input("Find your answer! Ask a yes or no question to the Magic 8 Ball: ")
    if x.endswith("?"):
        randomize()
        takeInput()
    else:
        print("Please input in a question format.")
        start()

# Main
start()