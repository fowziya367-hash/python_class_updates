data = ((10, 20), (5, 15, 25), (1, 2, 3, 4))

largest = data[0]

for t in data:
    if len(t) > len(largest):
        largest = t

print("Tuple with more numbers:", largest)
print("Number of numbers:", len(largest))