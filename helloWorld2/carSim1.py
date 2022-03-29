carStarted = False
carMoving = False
playerCommand = ""

print('Super Realistic Car Simulator, type help for commands!')
while playerCommand.lower() != 'exit':
    playerCommand = input('> ')
    if playerCommand.lower() == 'help':
        print('"Start" Starts the car')
        print('"Go" Moves the car')
        print('"Stop" Stops the car')
        print('"Exit" Ends the simulation')
    elif playerCommand.lower() == 'start':
        if carStarted:
            print('the car is already running, but you turn the key anyway')
            print('The engine makes a painful grinding noise')
        else:
            print('You start the car, it rumbles to life')
            carStarted = True
    elif playerCommand.lower() == 'stop':
        if carMoving:
            print('You slam on the breaks and the car screeches to a halt!')
        else:
            print('You slam on the breaks! but your not moving, so nothing happens...')
        carMoving = False
    elif playerCommand.lower() == 'go':
        if carStarted:
            if carMoving:
                print('The car keeps moving down the road')
            else:
                print('The car burns rubber as it accelerates down the road')
            carMoving = True
        else:
            print('You press the gas, but nothing happens. How odd...')
    elif playerCommand.lower() == 'exit':
        print("You throw yourself out of the vehicle")
        if carMoving:
            print("the car veers off the road and smashes into a tree")
    else:
        print('sorry Dave, i cant let you do that')

print('the end')