# 3/7/2022 10:11 PM EST

import random
import os

def save_password(name, password):
	txt_file = open("Passwords.txt", mode='a', encoding="utf-8")
	txt_file.write(name + ": " + password + ";\n")
	txt_file.close()

def main():
	characters = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	'v', 'w', 'x', 'y', 'z'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]

	password = ""
	name = input("What name do you want for your password? ")
	lenght = None

	while(type(lenght) != int):
		try:
			lenght = int(input("How long (in number of characters) do you want your password? "))
		except ValueError:
			print("That was not an integer number!")

	counter = 0

	while counter <= lenght:
		rand_00 = None
		rand_01 = None
		rand_00 = random.randint(0, len(characters) - 1)
		rand_01 = random.randint(0, len(characters[rand_00]) - 1)
		password += characters[rand_00][rand_01]
		counter += 1

	save_password(name, password)

	print("The generated password is \"" + password + "\" and was saved to a file")

	os.system("pause")

if __name__ == '__main__':
	main()

# 3/7/2022 11:15 PM EST
# 3/7/2022 11:22 PM EST - Changed the filemode from w to a
