scrambler = input('please provide you name: ')
first = scrambler[0]
second = scrambler[-1]
name = second + scrambler[1:-1] + first

endPlacer = len(scrambler)
startPlacer = 0

msg2 = ''
msg = f'Your name is {name.capitalize()} right?!?'
if endPlacer >= 5 :
    msg2 = "that's a long name"
else:
    msg2 = 'that is a short name'

print(msg)
print(msg2)