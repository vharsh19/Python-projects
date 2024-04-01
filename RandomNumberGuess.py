import random

randomNumber=random.randint(1,100)

while True:
    userGuess=int(input("Enter your Guess (or type QUIT to exit):"))
    if(userGuess=="QUIT"):
        break
    if(userGuess==randomNumber):
        print("Congratulations!! You Guessed the Number.")
        break
    elif(userGuess<randomNumber):
        print("The number you guessed is smaller that the answer.Take your Guess again")
    else:
        print("The number you guessed is larger that the answer.Take your guess again")
    
print("********GAME OVER*********")