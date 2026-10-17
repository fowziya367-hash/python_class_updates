def find_duplicate():
    s = "banana"
    for i in s:
        if s.count(i) > 1:
            return i

print(find_duplicate())