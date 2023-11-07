# Jan 10, 2023
# 10:08 a.m.

# This code is intended to calculate the summary information of a set of numbers

import random

class MyArray:
    def __init__(self, array):
        self.items = array
        
        self.mean = sum(array) / len(array)

        # sort a list in ascending order (i = original list)

        i = array

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

                c = 0 # start again
                continue

            elif c > 0 and c < len(i) - 1: # if we are moving an intermediate element

                if i[c] > i[c + 1]: # if it has to be moved to right
                    i[c] += i[c + 1]
                    i[c + 1] = i[c] - i[c + 1]
                    i[c] -= i[c + 1]

                if i[c] < i[c - 1]: # if it has to be moved to left
                    i[c] += i[c - 1]
                    i[c - 1] =+ i[c] - i[c - 1]
                    i[c] -= i[c - 1]

                    c = 0 # start again
                    continue

            elif c == len(i) - 1: # if we are moving the last element
                i[c] += i[c - 1]
                i[c - 1] = i[c] - i[c - 1]
                i[c] -= i[c - 1]

                c = 0 # start again
                continue

        if len(i) % 2 != 0:
            self.median = i[int(len(i) / 2 + 0.5) - 1]
        else:
            self.median = (i[int(len(i) /  2)] + i[int(len(i) / 2 + 1)]) / 2

        differences = [array[x] - self.mean for x in range(len(array))]
        differences_sqrd = [differences[x] ** 2 for x in range(len(differences))]
        self.variance = sum(differences_sqrd) / len(differences_sqrd)

        self.standard_deviation = self.variance ** 0.5
        
    def __repr__(self):
        return f"{self.items}\nMean: {self.mean}\nMedian: {self.median}\nVariance: {self.variance}\nStandard Deviation: {self.standard_deviation}"

myArray00 = MyArray([18, 24, 67, 55, 42, 14, 19, 26, 33])
print(myArray00)

# 11:32 a.m.
