



#1 imports at the
import random

#followed by any cosntants 
VALID_OPTIONS = ["rock", "paper", "scissors"]

#3 functions or classes


#4 main conditional 
if __name__ == "__main__":
    #only fun the code below if this file is being run directly from the command line
    # and not being imported from another file
    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        # exit()
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    # quick alias to facilitate some copy and pasting
    # we will soon move this into a function anyway
    u = user_choice
    c = computer_choice

    if u == "rock" and c == "rock":
        print("TIE GAME")
    elif u == "rock" and c == "paper":
        print("COMPUTER WINS")
    elif u == "rock" and c == "scissors":
        print("USER WINS")
    elif u == "paper" and c == "rock":
        print("COMPUTER WINS") # OOPS
    elif u == "paper" and c == "paper":
        print("TIE GAME")
    elif u == "paper" and c == "scissors":
        print("USER WINS") # OOPS
    elif u == "scissors" and c == "rock":
        print("COMPUTER WINS")
    elif u == "scissors" and c == "paper":
        print("USER WINS")
    elif u == "scissors" and c == "scissors":
        print("TIE GAME")