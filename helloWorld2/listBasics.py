names = ['Bob', 'John', 'Betty', 'John', 'Jon', 'Jhonny', 'Jhon', 'John', 'Mary']
namePlace = int(0)
print(names[-1])
print(names[2:])
print(names[:-2])
searchName = 'John'
# mission edit John to Jon
position = 0
johnExists = True
while johnExists:
    # find a John
    if names.__contains__(searchName):
        position2 = names.index(searchName)
        print(position2)
        foundName = names[position2]

        names[position2] = foundName.replace('h', '')
    else:
        johnExists = False
        # all the Johns have been eliminated




print(names)
# modName =