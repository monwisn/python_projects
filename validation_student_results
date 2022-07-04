data_valid = True

while data_valid:
    grade1 = input("Type the grade of the first test: ")

    try:
        grade1 = float(grade1)

    except ValueError as error:
        print(f"Invalid input: {error}")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = False

data_valid = True

while data_valid:
    grade2 = input("Type the grade of the second test: ")

    try:
        grade2 = float(grade2)

    except ValueError as error:
        print(f"Invalid input: {error}")
        continue

    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = False

data_valid = True

while data_valid:
    total_classes = input("Type the total number of classes: ")

    try:
        total_classes = int(total_classes)

    except ValueError as error:
        print(f"Invalid input: {error}")
        continue

    if total_classes <= 0:
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid = False

data_valid = True

while data_valid:
    absences = input("Type the number of absences: ")

    try:
        absences = int(absences)

    except ValueError as error:
        print(f"Invalid input: {error}")
        continue

    if absences < 0 or absences > total_classes:
        print("The number of absences can't be less than zero or grater than the number of total classes")
        continue
    else:
        data_valid = False


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print(f"Average grade: {round(avg_grade, 2)}")
print(f"Attendance rate: {str(round((attendance * 100), 2))}%")

if avg_grade >= 6 and attendance >= 0.8:
    print("The student has been approved")
elif avg_grade < 6 and attendance < 0.8:
    print("The student has failed due to an avarage grade lower than 6.0 and an attendance rate lower than 80%")
elif attendance >= 0.8:
    print("The student has failed due to an average grade lower than 6.0")
else:
    print("The student has failed due to an attendance rate lower than 80%")

