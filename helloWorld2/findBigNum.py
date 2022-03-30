# find the biggest number in a array or list
import random


arraySize = 100 # the size of the array to be generated
numSizeMult = 100 # range opf numbers to be generated (10 means 0-10)
theArray = list()

# make a list of numbers to search
for i in range(0, arraySize):
    tempNum = random.random() * numSizeMult
    # theArray[i] = tempNum
    theArray.append(tempNum)

print(theArray)

# search for the biggest number
bigNum = 0.0
for i in range(0, len(theArray)):
    if theArray[i] > bigNum:
        bigNum = theArray[i]
print('the biggest number in the list is...')
print(bigNum)