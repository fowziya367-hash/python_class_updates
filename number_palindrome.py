def palindrome(x):
    if x < 0:
        return False
    original = x
    reverse = 0
    while x > 0:
        a = x % 10
        reverse = reverse * 10 + a
        x = x // 10
    return original == reverse
x = int(input("Enter a number : "))
print(palindrome(x))