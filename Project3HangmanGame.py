import random
import Project3HangmanStages #importing different files
import Project3HangmanWords
# wordList=["apple", "potato", "beautiful"]
chosenWord=random.choice(ProjectHangmanWords.words) #accessing the imported files just like random
# print(chosenWord) #randomly chosen word from word list
display=[]
lives=6
for i in range(len(chosenWord)):
    display += '_'
print(display)
gameOver =False
while not gameOver:
    guessedLetter=input("Guess a letter: ").lower() #it will be converted to lower case
    for position in range(len(chosenWord)):
        letter=chosenWord[position]
        if(letter==guessedLetter):
            display[position]=guessedLetter
    print(display)
    if guessedLetter not in chosenWord:
        lives-=1
        if lives==0:
            gameOver=True
            print("You lose!!")
            print("correct word: "+ chosenWord)
    print(f"lives remaining= {lives}")
    if '_' not in display:
        gameOver=True
        print("You win!!")
    print(ProjectHangmanStages.stages[lives])

