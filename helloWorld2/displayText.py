screenWidth = 10
screenHeight = 10
playerLocationX = 1
playerLocationY = 9

pCommand = ''
while pCommand.lower() != 'exit':

    for y in range(screenHeight):
        lineWriter = ''
        for x in range(screenWidth):
            if (playerLocationX is x) and (playerLocationY is y):
                lineWriter += ' BOB '
            else:
                lineWriter += f'({x}.{y})'
        print(lineWriter)
    pCommand = input('press enter to continue, type "exit" to quit > ')
    playerLocationY -= 1
    playerLocationX += 1
