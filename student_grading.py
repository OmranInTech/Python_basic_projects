def grade_student(marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

# Input marks from the user
marks = float(input("Enter your marks: "))

# Get grade based on marks
grade = grade_student(marks)

print(f"Your grade is: {grade}")
