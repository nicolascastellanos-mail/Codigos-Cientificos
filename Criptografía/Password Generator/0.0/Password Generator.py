# feb 15 23:18

# Random password generator

from random import randint

while True:
    lenght = input("How long do you want the password to be? ")
    if lenght.isdigit:
        lenght = int(lenght)
    if not(isinstance(lenght, int)):
        print("Please, only integer numbers.")
        continue
    break

while True:
    letters = input("Do you want the password to have lowercases? ")
    if letters == 'y':
        letters = True
    break

while True:
    letters = input("Do you want the password to have uppercases? ")
    if letters == 'y':
        letters = True
    break

while True:
    numbers = input("Do you want the password to have numbers? ")
    if numbers == 'y':
        numbers = True
    break

while True:
    symbols = input("Do you want the password to have symbols? ")
    if symbols == 'y':
        symbols = True
    break

lowercases = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
uppercases = tuple(x.upper() for x in lowercases)
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
symbols = ('!', '@', '#', '$')
characters = (lowercases, uppercases, numbers, symbols)

password = str()
for x in range(12):
    a = randint(0, 3)
    b = randint(0, len(characters[a]) - 1)
    password += characters[a][b]

print("Your generated password is: ", password)

# feb 15 23:52
