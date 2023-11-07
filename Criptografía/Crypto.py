# 07/17/2022. 8:15 PM
# Intended for creating an email direction

from os import system
from random import randint

char = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
orig = input()
ekey = randint(0, 28)
encr = ""
indx = 0
cont = 0
fkey = "K"

while cont < len(orig):
	indx = char.index(orig[cont])
	indx += ekey
	encr += char[indx]
	fkey += " " + str(ekey)
	ekey = randint(0, 28)
	cont += 1

print(encr)
print(fkey)

system("pause")

# 8:39
# Easy
# 8:44 - 8:54
# Added random
