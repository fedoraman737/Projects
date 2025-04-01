import random

randomNumber = random.randint(1, 10)
playerGuess = 0
guessedCorrectly = False
attemptsMade = 1

while guessedCorrectly == False:
    playerGuess = int(input("Guess a number! "))
    if playerGuess == randomNumber:
        print("You guessed correctly! Now go make a keygen")
        print("Your total guesses to figure this out =",attemptsMade)
        guessedCorrectly = True
    elif attemptsMade >= 10:
        print("TOO MANY ATTEMPTS GO TOUCH SOME GRASS")
    else:
        difference = abs(playerGuess - randomNumber)
        if difference == 0:
            print("Correct!")
        elif difference <= 2:
            print("🔥 Hot!")
        elif difference <= 5:
            print("🌡️ Warm")
        else:
            print("❄️ Cold")
