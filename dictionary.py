students = {
    "Fowzi": {
        "department": "B.Sc CS",
        "marks": {"Python": 80, "Java": 75, "Maths": 85}
    },
    "Keerthi": {
        "department": "BCA",
        "marks": {"Python": 70, "Java": 80, "Maths": 75}
    }
}

for name, details in students.items():
    total = sum(details["marks"].values())

    print("Student:", name)
    print("Department:", details["department"])
    print("Subject Marks:", details["marks"])
    print("Total Mark:", total)
    print()