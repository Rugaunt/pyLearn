import random
"""
builds a random array of integers and removes duplicate numbers from the list
"""

arraySize = 100 # the size of the array to be generated
numSizeMult = 10 # range opf numbers to be generated (10 means 0-10)
theArray = list()

# make a list of numbers to search
for i in range(0, arraySize):
    tempNum = int(random.random() * numSizeMult)
    theArray.append(tempNum)

print('the generated list is: ')
print(theArray)
# for each whole number
for i in range(0, numSizeMult):
    # check for duplicates
    numSize = theArray.count(i)
    print(str(numSize) + ' duplicates of ' + str(i) + ' found...')
    while numSize > 1:
        # found duplicates, time to remove them
        theArray.remove(i)
        numSize -= 1
    else:
        print('   No duplicates of ' + str(i) + ' left!')

print(theArray)