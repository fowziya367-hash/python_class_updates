word = input("Enter a word: ")

for i in word:
    if word.count(i) > 1:
        print(i)