marks = [45, 78, 92, 55, 88]

pass_marks= 50

for i in marks:
    if i < pass_marks:
        print(i, "- Fail")
    else:
        print(i, "- Pass")

average = sum(marks)/len(marks)
print("Averange", average)