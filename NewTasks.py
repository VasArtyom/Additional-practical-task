grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
AaronGrades = sum(grades[0]) / len(grades[0])
BilboGrades = sum(grades[1]) / len(grades[1])
JohnnyGrades = sum(grades[2]) / len(grades[2])
KhendrikGrades = sum(grades[3]) / len(grades[3])
SteveGrades = sum(grades[4]) / len(grades[4])
result = {students[0] : AaronGrades,
          students[1] : BilboGrades,
          students[2] : JohnnyGrades,
          students[3] : KhendrikGrades,
          students[4] : SteveGrades}
print(result)


