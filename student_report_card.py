

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


names = ["prashant", "hari", "sam", "sita", "ram"]
marks = [85, 62, 45, 71, 91]


for i in range(len(names)):
    name = names[i]
    mark = marks[i]
    print("Name:", name, "| Marks:", mark, "| Grade:", get_grade(mark))

print("Class Average:", sum(marks) / len(marks))