name = input("Enter student name: ")
Tamil = int(input("Enter Tamil mark: "))
English = int(input("Enter English mark: "))
Python = int(input("Enter Python mark: "))
Maths = int(input("Enter Maths mark: "))

total = Tamil + English + Python + Maths
average = total / 4

print("\n----- STUDENT MARK DETAILS -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)

if Tamil < 35 or English < 35 or Python < 35 or Maths < 35:
    print("Result: FAIL")
elif average >= 90:
    print("Grade: A+")
    print("Result: PASS")
elif average >= 80:
    print("Grade: A")
    print("Result: PASS")
elif average >= 70:
    print("Grade: B")
    print("Result: PASS")
elif average >= 60:
    print("Grade: C")
    print("Result: PASS")
else:
    print("Grade: D")
    print("Result: PASS")