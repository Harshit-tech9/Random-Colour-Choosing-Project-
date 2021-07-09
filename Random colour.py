import random

colour = ["Red", "Yellow", "Pink", "Grey", "Purple", "Orange", "Maroon", "White"]


while True:
    color = colour[random.randint(0, len(colour)-1)]
    guess = input("Enter the choice of your colour: ")

    while True:
        if (guess == color):
            print("The Choice of your colour is ", color)
            break

        else:
            guess = input("Your Guess is Incorrect, Please try again")

    print("Your Guess is Correct: ", color)

    try_again = input("Do you want to try again? Type 'no' to quit")

    if try_again == 'no' :
        break

print("Thanks for Playing with us. See you again :)")
