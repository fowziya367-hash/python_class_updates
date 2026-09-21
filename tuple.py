tuples = ((10, 20), (5, 15, 25), (1, 2, 3, 4))

max_tuple = tuples[0]

for t in tuples:
    if len(t) > len(max_tuple):
        max_tuple = t

print("Tuple with more numbers:", max_tuple)
print("Number of numbers:", len(max_tuple))