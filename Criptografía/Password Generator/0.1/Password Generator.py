# feb 15 23:18

# Random password generator

from random import randint

while True:
    lenght = input("How long do you want the password to be? ")
    if lenght.isdigit():
        lenght = int(lenght)
    else:
        print("Please, only integer numbers.")
        continue
    break

print("For the following questions, answer 'y' to indicate a positive answer. Any other answer will be taken as negative.")

while True:
    lowercases = input("Do you want the password to have lowercases? ")
    if lowercases == 'y':
        lowercases = True
    break

while True:
    uppercases = input("Do you want the password to have uppercases? ")
    if uppercases == 'y':
        uppercases = True
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

characters = list()

if lowercases:
    lowercases = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    characters.append(lowercases)
if uppercases:
    uppercases = tuple(x.upper() for x in lowercases)
    characters.append(uppercases)
if numbers:
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    characters.append(numbers)
if symbols:
    symbols = ('!', '@', '#', '$')
    characters.append(symbols)

password = str()
for x in range(lenght):
    a = randint(0, len(characters) - 1)
    b = randint(0, len(characters[a]) - 1)
    password += characters[a][b]

print("Your generated password is: ", password)

# feb 15 23:52

# feb 16 14:59 (0.1)
# feb 16 15:10 (0.1)
