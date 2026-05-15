# marks = [45, 78, 92, 55, 88]

# pass_marks= 50

# for i in marks:
#     if i < pass_marks:
#         print(i, "- Fail")
#     else:
#         print(i, "- Pass")

# average = sum(marks)/len(marks)
# print("Averange", average)


# Day 4 practice


# def add(a,b):
#     result = a + b 
#     return result
# answer = add(10, 5)
# print(answer)


# print(add(100 , 200))
# print(add(7, 3))



# def calculate_average(marks):
#     average = sum(marks) / len(marks)
#     return average

# def check_pass(mark):
#     if mark >= 50:
#         return "pass"
#     else:
#         return "Fail"

# my_marks = [45, 78, 92, 55, 88]

# for mark in my_marks:
#     print(mark, "-", check_pass(mark))


# print("Average:", calculate_average(my_marks))



#### Day 5 Loop through a dictionary 


# student = {
#     "name": "prashant",
#     "age": 21,
#     "course": "data science",
#     "gpa": 3.5
# }


# for key, value in student.items():
#     print(key, ":", value)



students = [
    {"name": "Prashant", "marks": 85},
    {"name": "Hari", "marks": 62},
    {"name": "Sita", "marks": 45},
    {"name": "Ram", "marks": 91}
]

for student in students:
    if student["marks"] >= 50:
        print(student["name"], "-", student["marks"], "-", "pass")
    else:
        print(student["name"], "-", student["marks"], "-", "Fail")

  


