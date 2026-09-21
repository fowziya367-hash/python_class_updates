project1 = {"Arun", "Guna", "Fowzi"}
project2 = {"Guna", "Fowzi", "David"}
project3 = {"Guna", "Keerthi"}

employee = "Guna"
count = 0

projects = [project1, project2, project3]

for project in projects:
    if employee in project:
        count = count + 1

print(employee, "is working in", count, "projects")