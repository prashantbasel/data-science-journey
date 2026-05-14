def greet(name):
    print("Hello", name)
    print("welcome to day 4")
greet("Prashant")
greet("sam")
greet("ram")


def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

def check_pass(mark):
    if mark >= 50:
        return "pass"
    else:
        return "Fail"

my_marks = [45, 78, 92, 55, 88]

for mark in my_marks:
    print(mark, "-", check_pass(mark))


print("Average:", calculate_average(my_marks))
