# magic-8-ball
This is a Magic 8 Ball program that generates random answers from a predefined list of responses and provides a user-friendly interface for asking questions and receiving answers.

Inside the loop:
Prompts the user to enter a yes-or-no question (stored in a variable)
Uses an if statement and the endswith() function to check if the question ends with a question mark. If not, it asks the user to re-enter the question.
Uses random.choice() with the responses list to select a random response.
Displays the selected response to the user.
Prompts the user if they want to ask another question. If the response is "No", it exits the loop.
