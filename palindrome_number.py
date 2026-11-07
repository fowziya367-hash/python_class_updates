def palindrome(x,y=0):
    if x == 0:
        return y
    a = x % 10
    b = y * 10 + a
    return palindrome (x // 10, b)
x = int(input("Enter a number : "))
if x < 0 :
    print("False")
else :
    if x == palindrome(x):
        print("True")
    else :
        print("False")