import csv

def read_students_from_file(filename):
    students = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, sexo = row
                    students.append({"name": name, "sexo": sexo})
                else:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return students

def main():
    filename = "exemplo5.csv"
    students = read_students_from_file(filename)
    
    if students:
        for student in sorted(students, key=lambda student: student["name"]):
            print(f'{student["name"]}: {student["sexo"]}')
    else:
        print("No students found.")

if __name__ == "__main__":
    main()