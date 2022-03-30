names = ['Bob', 'John', 'Betty', 'Mary']
namePlace = int(0)
print(names[-1])
print(names[2:])
print(names[:-2])
searchName = 'John'
# mission edit John to Jon
position = 0
for namePlace in names:
    print('is this John?')
    print(namePlace)
    print('it is ' + names[namePlace])
    if names[namePlace] == searchName:
        position = namePlace

foundName = names[position]
foundName.replace('h', '')
names[position] = foundName

print(names)
# modName =