""" 10/04/2022, 2:37 p.m. """

from random import randint

def mix(input_list):
	already = []
	result = []
	counter = 0
	random = 0

	while counter < len(input_list):
		random = randint(0, len(input_list) - 1)

		while random in already:
			random = randint(0, len(input_list) - 1)

		result.append(input_list[random])
		already.append(random)

		counter += 1

	return result

def sort(input_list):
	print("The original list is " + str(input_list))
	counter = 0
	print("Analising " + str(input_list[counter]))

	if input_list[counter] > input_list[counter + 1]:
		print(str(input_list[counter]) + " is greater than "\
			+ str(input_list[counter + 1]) + " and will get moved to the right")
		input_list[counter] += input_list[counter + 1]
		input_list[counter + 1] = input_list[counter] - input_list[counter + 1]
		input_list[counter] -= input_list[counter + 1]
	else:
		print(str(input_list[counter]) + " is not greater than "\
			+ str(input_list[counter + 1]) + " and will not get moved to the right")

	print("The list is now " + str(input_list))

	counter += 1

	while counter < len(input_list) - 1:
		if counter > 0:
			if input_list[counter] < input_list[counter + 1] and\
			input_list[counter] > input_list[counter - 1]:
				print(str(input_list[counter]) + " is in its right position and will not be moved")
				counter += 1
				continue
		elif counter == len(input_list) - 1:
			if input_list[counter] > input_list[counter - 1]:
				print(str(input_list[counter]) + " is in its right position and will not be moved")
				counter += 1
				continue
		else:
			if input_list[counter] < input_list[counter + 1]:
				print(str(input_list[counter]) + " is in its right position and will not be moved")
				counter += 1
				continue

		print("Analising " + str(input_list[counter]))

		if input_list[counter] > input_list[counter + 1]:
			print(str(input_list[counter]) + " is greater than "\
				+ str(input_list[counter + 1]) + " and will get moved to the right")
			input_list[counter] += input_list[counter + 1]
			input_list[counter + 1] = input_list[counter] - input_list[counter + 1]
			input_list[counter] -= input_list[counter + 1]
		else:
			print(str(input_list[counter]) + " is not greater than "\
				+ str(input_list[counter + 1]) + " and will not get moved to the right")

		print("The list is now " + str(input_list))

		if counter > 0:
			if input_list[counter] < input_list[counter - 1]:
				print(str(input_list[counter]) + " is smaller than "\
					+ str(input_list[counter - 1]) + " and will get moved to the left")
				input_list[counter] += input_list[counter - 1]
				input_list[counter - 1] = input_list[counter] - input_list[counter - 1]
				input_list[counter] -= input_list[counter - 1]
			else:
				print(str(input_list[counter]) + " is not smaller than "\
					+ str(input_list[counter - 1]) + " and will not get moved to the left")

		print("The list is now " + str(input_list))
		print("Re-analising from the beginning")
		counter = 0
		continue

	if input_list[counter] > input_list[counter - 1]:
		print(str(input_list[counter]) + " is in its right position and will not be moved")

	sorted_list = input_list
	
	return sorted_list

""" 10/04/2022, 3:37 p.m. """
