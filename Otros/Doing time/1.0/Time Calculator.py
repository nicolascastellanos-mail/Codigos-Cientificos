# Finally getting inspired :3
# 26/11/2022 at 1:40 p.m.
# This is a time calculator ^-^

from os import system
from time import sleep

def main_menu():
	print("Time Calculator - By Castellanos")
	print()
	print("1) Use")
	print("2) Examples")
	print("3) Exit")
	print()

	try:
		option = int(input("Choose an option! "))
	except:
		non_valid()
		return main_menu()

	if option == 1:
		return use()
	elif option == 2:
		return examples()
	elif option == 3:
		return bye()
	else:
		non_existing()
		return main_menu()

def use():
	system("cls")
	print("You're welcome ^-^")
	print()
	calculation = input("Enter some text: ")
	print()
	print("Wanna return to the main menu? (Press any key)")
	system("pause >nul")
	system("cls")
	return main_menu()

def examples():
	system("cls")
	print("Here are some examples on how to use it UwU")
	print()
	print("These are some valid entries:")
	print()
	print("- 6h 43m 12s")
	print()
	print("Randomly generated entries very soon")
	print()
	print("Wanna return to the main menu? (Press any key)")
	system("pause >nul")
	system("cls")
	return main_menu()

def non_valid():
	system("cls")
	print("Not a valid entry!")
	sleep(1)
	system("cls")

def non_existing():
	system("cls")
	print("Not an existing option!")
	sleep(1)
	system("cls")

def bye():
	system("cls")
	print("Bye bye!")
	print(";3")
	sleep(0.25)
	system("cls")
	exit()

def main():
	main_menu()

if __name__ == '__main__':
	main()
	system("cls")
	print("Some exception has occurred!")
	print("Pressing ENTER will exit this program!")
	system("pause >nul")

# Finishing 1.0 (only menus)
# 26/11/2022 at 2:27 p.m.
