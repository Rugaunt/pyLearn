scrambler = input('please provide you name: ')
first = scrambler[0]
second = scrambler[-1]
name = second + scrambler[1:-1] + first

endPlacer = len(scrambler)
startPlacer = 0

msg2 = ''
msg = f'Your name is {name.capitalize()} right?!?'
if endPlacer >= 5 :
    msg2 = "that is a long name"
else:
    msg2 = 'that is a short name'

print(msg)
print(msg2)

print('string method basics:')
print(msg2.upper())
print(msg2.lower())
print(msg2.title())
print(msg2.find('that'))
print(msg2.replace('that', name))
if "B" in msg2:
    print("there's a bee in there!")
else:
    print("no bees in here...")
if "b" in msg:
    print("but you have a bee!")
else:
    print("no bees over there...")
