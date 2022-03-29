import random

winningNumber: int = 9
ranWinNum = int(random.random() * 10)
print('psst psst... the number is ' + str(ranWinNum))
guessCount: int = 0
guessLimit = 3
while guessCount < guessLimit:
    guessCount += 1
    guess = int(input('what number am i thinking of? '))
    guess = int(guess)
    if guess == ranWinNum:
        print('you got it!')
        break
    else:
        print('nope! ' + str(guess) + " isn't the number")

else:
    print('you lose!')