student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

outstanding = [x for x in range(91,101)]
Exceeds_expectations = [x for x in range(81,91)]
Acceptable = [x for x in range(71,81)]
Fail = [x for x in range(71)]

school_grades = {
    "outstanding": outstanding,
    "Acceptable": Acceptable,
    "Exceeds_expectations": Exceeds_expectations,
    "Fail": Fail
}

student_grades = {}

# Check if a student belongs to a grade
for k,v in student_scores.items():
    for grade_name, grade_value in school_grades.items():
        if v in grade_value:
            student_grades[k] = grade_name
            break
print(student_grades)