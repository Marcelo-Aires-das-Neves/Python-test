students = []

with open("exemplo5.csv") as file:
    for line in file:
        name, sexo = line.strip().split(",")
        student = {"name": name, "sexo": sexo}
        students.append(student)
            
    for student in sorted(students, key=lambda student: student["sexo"]):
        print(f'{student["name"]}: {student["sexo"]}')
        