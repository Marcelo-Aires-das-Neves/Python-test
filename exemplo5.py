import csv

students = []

with open('exemplo5.csv') as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "sexo": sexo})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f'{student["name"]}: {student["sexo"]}')