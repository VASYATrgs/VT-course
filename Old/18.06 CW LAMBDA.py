students = [
    {"имя": "Алиса", "оценка": 85},
    {"имя": "Борис", "оценка": 75},
    {"имя": "Виктор", "оценка": 95},
    {"имя": "Vuti", "оценка": 95},
    {"имя": "Kloin", "оценка": 95}
]

sorted_by_grade = sorted(students, key=lambda student: student["имя"], reverse=True)
print(sorted_by_grade)

x=int(input())
y=int(input())
z=int(input())
add = lambda x, y, z: (x + y + z)/2

print(add(x, y, z))



students = [
    {"имя": "Алиса", "оценка": 85},
    {"имя": "Борис", "оценка": 75},
    {"имя": "Виктор", "оценка": 95},
]

sorted_by_grade = sorted(students, key=lambda student: student["имя"], reverse=True)
