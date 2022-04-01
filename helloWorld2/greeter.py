def intro(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("Welcome Aboard!")


print('start')
intro("John", "Smith")


print("keyword argument usage")
print('increases readability of code')


def calc_cost(price, quantity, discount):
    total = (price * quantity) * (discount / 100)
    print("total: " + str(total) + '$')


calc_cost(price=50, quantity=5, discount=5)

print("return usage")
print('wd')


def square(num):
    return num * num


print(square(4))
whatsTheSquare = square(4)
print(whatsTheSquare)
