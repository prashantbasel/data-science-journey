## first way to open a file

# file = open("students.csv", "r")
# content = file.read()
# file.close

# print(content)


## better way to open a file 


# with open("students.csv", "r") as file:
#     for line in file:
#         print(line)


## professional way 


# import csv

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], "scored", row["marks"], "in", row["city"])



# import csv

# students = [
#     {"name": "Prashant", "marks": 85, "grade": "A"},
#     {"name": "Hari", "marks": 62, "grade": "B"},
#     {"name": "Sita", "marks": 45, "grade": "Fail"},
#     {"name": "Ram", "marks": 91, "grade": "A"},
#     {"name": "Maya", "marks": 73, "grade": "B"}
# ]

# with open("results.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "marks", "grade"])
#     writer.writeheader()
#     writer.writerows(students)

# print("File saved successfully")





import csv

def get_grade(mark):
    mark = int(mark)
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# Read students.csv
students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["grade"] = get_grade(row["marks"])
        students.append(row)

# Write results.csv
with open("results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks", "city", "grade"])
    writer.writeheader()
    writer.writerows(students)

print("Done. Results saved to results.csv")