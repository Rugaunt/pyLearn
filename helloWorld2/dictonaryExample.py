"""
Name: John Smith
Email: erfuh@vrij.cot
Phone: 111-444-2211
"""

customer = {
    "namE": "John Smith",
    "age": 30,
    "is_verified": False
}

print(customer["namE"])
#                   key      default
print(customer.get("name", "Unknown"))

numbers = {
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine"
}

phone = input("Phone# ")
# phone = int(phone)
output = ""
for ch in phone:
    output += numbers.get(ch, "!") + ' '

print(output)