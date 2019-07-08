"""
* First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.
* Then the user has to find out what this number is (using input()). Store user's guess in a variable called guess.
* Check if your secret is equal to user's guess.
* If the user's guess is wrong, let him/her know that (use print() and if/else).
* If the user's guess is correct, congratulate him/her.
"""

secret = 88

guess = int(input("Which number you guess?"))

if guess == secret:
    print("Yes, this was the right number!")
else:
    print("Sorry, no - just try again!")