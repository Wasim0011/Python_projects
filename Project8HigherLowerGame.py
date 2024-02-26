import random   #for generating random number
import os  #for accessing clear screen function(sometimes it may not work properly)

import Project8Art  #for accessing other files
import Project8DataBase

SCORE = 0   #declaring as global variable

print(Project8Art.game_logo)

#defining some functions
def display_account_info(account):
    name = account['name']
    description = account['Description']
    country = account['Country']
    return (f"{name}, a {description}, from {country}")

def check_answer(guess, followers1, followers2):
    if followers1>followers2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False

continue_flag=True
account2 = random.choice(Project8DataBase.data)
while continue_flag:    #since we want to play till we guess correctly
    account1 = account2
    account2 = random.choice(Project8DataBase.data)
    while account1 == account2:
        account2 = random.choice(Project8DataBase.data)
    # print(account1)
    # print(account2)
    print(f"Compare1: {display_account_info(account1)}")
    print(Project8Art.vs)
    print(f"Compare2: {display_account_info(account2)}")
    guess = int(input("Who has more followers? Type 1 or 2: "))
    followers1 = account1['follower_count']
    followers2 = account2['follower_count']
    # print(followers1)
    # print(followers2)
    os.system('cls')    #clearing screen
    print(Project8Art.game_logo)
    is_correct = check_answer(guess, followers1, followers2)
    if is_correct:
        SCORE +=1
        print(f"You are right. Your score is: {SCORE}")
    else:
        print(f"Your are wrong. Your final score is: {SCORE}")
        continue_flag = False
