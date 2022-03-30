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
# john returns to the party
print('a wild john appears!')
names.append('John')

# and another!
names.insert(0, 'John')
print(names)

# how many Johns are there?
print(names.count(searchName))

# ok ok everybody line up in order!!
names.sort()
print(names)
# let me take attendance
names2 = names.copy()
# no no no, the other way!
names.reverse()
print(names)

# nah, lets get rid of them
names.remove('John')
print(names)

# there are too many people at the party, lets get rid of the last one
names.append('Vanessa')
names.pop()
print(names)

# i still think there is a john at the party... where is he?
whereIsHe = names.index(searchName)
print(whereIsHe)
# is there a Jon at the party
isJon = ('Jon' in names)
print(isJon)
# but is there a John here?
isJohn = searchName in names
print(isJohn)
# actually lets cancel the whole party
names.clear()
print(names)
# modName =