# def stupid_addition(a, b):
#     if type(a)==str and type(b)==str:
#         print(int(a) + int(b))
#     elif type(a)==int and type(b)==int:
#         print(str(a) + str(b))
#     else:
#         print("None")

# stupid_addition(4, 6)


"""
Assumption:
 

Plan:
- Might look at a different logic for replaying versus playing for the first time
- Might look at collect user input about game settings(min, max)

"""
# Need to import random module
import random

is_playing = True
# need the main game while loop
while is_playing:


     # give game start message to user that explains the game and what is expected 
    print("Welcome to GUESS THE NUMBER! I hope you have fun!")
     
     # initialize a random number at the start of the of the game
    number_to_guess = random.randint(1, 100)

    user_has_won = False

     # need a guessing loop that runs until user guesses correctly (while loop?)
    while not user_has_won:
        # promt the user for  their input 
        user_guess = int(input("I'm thinking of a number between 1 and 100. Guess which number I'm thinking of:"))

        # TODO: provide data to the user about the game
        # TODO: do some error checking on the user input 

        # if user guess is wrong 
        if user_guess == number_to_guess:
            user_has_won = True
            # program alerts user that guess wrong if it was too high or too low
            print("You guessed right! Good job!")

            play_again =  input("Would you like to play again? Y or N?")
            if play_again.lower() == "n":
                is_playing = False
        # if user guess is right 
        elif user_guess > number_to_guess:
            print("Your guess was to high! Try again!")
        else: 
            print("Your guess is too low! Try again")
            # program alerts iset they won and asks if the want to play again or exit


