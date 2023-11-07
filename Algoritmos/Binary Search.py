# March 4, 2023. 19:52

def binary_search(l, e):
    i = int(len(l) / 2)
    while True:
        if l[i] == e:
            return i
        if l[i] < e:
            return binary_search(l[i:], e)
        elif l[i] > e:
            return binary_search(l[:i], e)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(l, 2))

# March 4, 2023. 19:59
