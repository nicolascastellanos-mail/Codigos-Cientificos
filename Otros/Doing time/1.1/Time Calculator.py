# Finally getting inspired :3
# 26/11/2022 at 2:28 p.m.
# This is a time calculator ^-^

from os import system
from time import sleep
from re import findall

class time_expression():
	def __init__(self, raw_entry):
		self.hours = int(findall("([0-9]*)h[0-9]*m[0-9]*s", raw_entry)[0])
		self.minutes = int(findall("[0-9]*h([0-9]*)m[0-9]*s", raw_entry)[0])
		self.seconds = int(findall("[0-9]*h[0-9]*m([0-9]*)s", raw_entry)[0])
		if self.seconds >= 60:
			self.minutes += self.seconds // 60
			self.seconds = self.seconds % 60
		if self.minutes >= 60:
			self.hours += self.minutes // 60
			self.minutes = self.minutes % 60
	def __repr__(self):
		return f"{self.hours}h{self.minutes}m{self.seconds}s"
	def __str__(self):
		return f"{self.hours}h{self.minutes}m{self.seconds}s"
	def __add__(self, another_object):
		hours = self.hours + another_object.hours
		minutes = self.minutes + another_object.minutes
		seconds = self.seconds + another_object.seconds
		return time_expression(f"{hours}h{minutes}m{seconds}s")
	def __sub__(self, another_object):
		hours = self.hours - another_object.hours
		minutes = self.minutes - another_object.minutes
		seconds = self.seconds - another_object.seconds
		return time_expression(f"{hours}h{minutes}m{seconds}s")

def polish(raw_entry):
	words = raw_entry.split()
	symbols = ("+", "-")
	objects = list()

	for word in words:
		if findall("[0-9]*h[0-9]*m[0-9]*s", word):
			temporal_object = time_expression(word)
			objects.append(temporal_object)
		elif word in symbols:
			objects.append(word)
		else:
			non_valid()
			return use()

	return objects

def solve(entry):
	entry_copy = entry
	while len(entry_copy) != 1:
		first_operand = entry_copy[0]
		operation = entry_copy[1]
		second_operand = entry_copy[2]
		if operation == "+":
			entry_copy = [first_operand + second_operand] + entry_copy[3:]
		elif operation == "-":
			entry_copy = [first_operand - second_operand] + entry_copy[3:]
	return entry_copy

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
	raw_entry = input("Enter some text: ")
	print()
	entry = polish(raw_entry)
	result = solve(entry)
	print("This is your result OwO")
	print()
	print(solve(entry)[0])
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

if __name__ == "__main__":
	main()
	system("cls")
	print("Some exception has occurred!")
	print("Pressing ENTER will exit this program!")
	system("pause >nul")
	system("cls")

# Finishing 1.0 (only menus)
# 26/11/2022 at 2:27 p.m.
# Finishing 1.1 (solving addition and subtraction)
# 26/11/2022 at 5:08 p.m. (took a rest half of the time)
