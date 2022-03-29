print('operands')
x = input('first number: ')
y = input('second number: ')
x = float(x)
y = float(y)
print('addition')
addExample = x + y
print(addExample)
print('subtraction')
subtractExample = x - y
print(subtractExample)
print('division')
divExample = x / y
print(divExample)
print('division (integer)')
intDivExample = x // y
print(intDivExample)
print('modulus')
modExample = x % y
print(modExample)
print('multiplication')
multExample = x * y
print(multExample)
print('powers to')
powerExample = x ** y
print(powerExample)
roundExample = round(divExample)
absExample = abs(divExample)
print('rounded division is ' + str(roundExample) + " and absolute value [z] is " + str(absExample))
