import random
import Project7Logo_art #importing file
EASY_LEVEL_ATTEMPTS=10  #global variable
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(levelChosen):    #function to set difficulty level
    if levelChosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif levelChosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def checkAnswer(num, guess, attempts, level):  #function to check answer
    if guess>num:
        print("Your guess is Too High")
        return attempts-1
    elif guess<num:
        print("Your guess is Too Low")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {num}")
        print(f"You guessed in {set_difficulty(level)-attempts+1} attempts!!")  #counting attempts

def game(): #function to play game
    print(Project7Logo_art.logo)    #printing text to ascii art by using imported file
    print("Let me think of a number between 1 to 50")
    num=random.randint(1, 50)   #choosing any random number between, 1 to 50 (both inclusive)
    level=input("Choose level of difficulty...Type 'easy' or 'hard': ").lower() #converting to lower case
    attempts=set_difficulty(level)  #setting difficulty level
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS: #when user enters wrong difficulty level
        print("You have entered wrong difficulty level... Play again!!")
        level=input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
        attempts=set_difficulty(level)
    guess=0;    #for using guess in while loop
    while guess!=num:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=int(input("Guess a number: "))    #converting into integer
        attempts=checkAnswer(num, guess, attempts, level)  #attempts will decrease on calling checkAnswer function
        if attempts==0:
            print("You are out of guesses... You lose!")
            return
        elif guess!=num:
            print("Guess again")

game()  #call function to play game


