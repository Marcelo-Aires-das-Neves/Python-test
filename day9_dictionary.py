student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def get_grade(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"

for student, score in student_scores.items():
    student_grades[student] = get_grade(score)

# Print the final grades
for student, grades in student_grades.items():
    print(f"{student} {student_scores[student]}: {grades}")