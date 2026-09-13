balance = 8000
while balance > 0:
    amount = int(input("Enter withdrawl amount: "))
    if amount <= balance:
        print("withdrawl successful")
        print("Remaining Balance =",balance)
    else:
        print("Insufficient Balance")