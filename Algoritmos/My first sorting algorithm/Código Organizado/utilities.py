import random

def generate(i, s):
	c = 1

	while c <= s:
		i.append(c)
		c += 1

	return i

def mix(i):
	# mix a list ( i = original list)

	c = 0 # a counter
	r1 = 0 # just a random number
	r2 = 0 # and... another one

	while c < len(i) * 1000: # mix 1000 times the number of elements
		r1 = random.randint(0, len(i) - 1) # generate the first random number
		r2 = random.randint(0, len(i) - 1) # generate the first random number

		while r1 == r2:
			r1 = random.randint(0, len(i) - 1) # generate the first random number
			r2 = random.randint(0, len(i) - 1) # generate the first random number

		i[r1] += i[r2]
		i[r2] = i[r1] - i[r2]
		i[r1] -= i[r2]

		c += 1

	return i

def sort(i):
	# sort a list in ascending order (i = original list)

	c = 0 # a counter

	while c < len(i) - 1: # access all elements

		# check if the element is in the right position

		if c == 0: # if we are checking the first element

			if i[c] < i[c + 1]:
				c += 1
				continue

		elif c > 0 and c < len(i) - 1: # if we are checking an intermediate element

			if i[c] < i[c + 1] and i[c] > i[c - 1]:
				c += 1
				continue

		elif c == len(i) - 1: # if we are checking the last element

			if i[c] > i[c - 1]:
				c += 1
				continue

		# if it is not in the right position, the execution will pass to here

		if c == 0: # if we are moving the first element
			i[c] += i[c + 1]
			i[c + 1] = i[c] - i[c + 1]
			i[c] -= i[c + 1]

			return i

		elif c > 0 and c < len(i) - 1: # if we are moving an intermediate element

			if i[c] > i[c + 1]: # if it has to be moved to right
				i[c] += i[c + 1]
				i[c + 1] = i[c] - i[c + 1]
				i[c] -= i[c + 1]

			if i[c] < i[c - 1]: # if it has to be moved to left
				i[c] += i[c - 1]
				i[c - 1] = i[c] - i[c - 1]
				i[c] -= i[c - 1]

			return i

		elif c == len(i) - 1: # if we are moving the last element
			i[c] += i[c - 1]
			i[c - 1] = i[c] - i[c - 1]
			i[c] -= i[c - 1]

			return i

	return 0

def draw(i):
	s = ""
	c = 0

	while c < len(i):

		while len(s) < i[c]:
			s += "-"

		if s == "":
			print("")

		else:
			print(s)

		s = ""

		c += 1
