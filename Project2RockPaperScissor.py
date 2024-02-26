import random
print("**Enter 0 for Rock, 1 for Paper and 2 for Scissor**")
computer = random.randint(0, 2)
# print(computer)
# print(type(computer))
user = int(input("Enter your choice: "))
# print(type(user))
print(f"You chose: {user} and Computer chose: {computer}")
if user < 0 or user > 2:
    print("You have entered a wrong input and you LOSE the game")
elif user == computer:
    print("You and computer chose the same and match is DRAW")
elif user == 0 and computer == 2:
    print("You WIN the game")
elif user == 2 and computer == 0:
    print("You LOSE the game")
elif computer > user:
    print("You LOSE the game")
elif user > computer:
    print("You WIN the game")
