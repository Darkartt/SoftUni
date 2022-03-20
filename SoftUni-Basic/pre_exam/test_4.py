students_in_exam = int(input())

grade_min_5 = 0
grade_min_4 = 0
grade_min_3 = 0
grade_under_3 = 0

grade_counter = 0

for student in range(students_in_exam):
    grade = float(input())
    grade_counter += grade
    if grade >= 5:
        grade_min_5 += 1
    elif grade >= 4:
        grade_min_4 += 1
    elif grade >= 3:
        grade_min_3 += 1
    else:
        grade_under_3 += 1

print(f"Top students: {grade_min_5 / students_in_exam * 100:.2f}%")
print(f"Between 4.00 and 4.99: {grade_min_4 / students_in_exam * 100:.2f}%")
print(f"Between 3.00 and 3.99: {grade_min_3 / students_in_exam * 100:.2f}%")
print(f"Fail: {grade_under_3 / students_in_exam * 100:.2f}%")
print(f"Average: {grade_counter / students_in_exam:.2f}")