# this programm will print out scores of students

print("Welcome to the student grading programm :D")

student_scores : dict = {
    "Harry"     : 81,
    "Ron"       : 78,
    "Hermione"  : 99,
    "Draco"     : 74,
    "Neville"   : 62
}

student_grades : dict = {}

for key in student_scores:
    score : int = student_scores[key]
    if score >= 91 and score <= 100:
        student_grades[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[key] = "Acceptable"
    elif score <= 70:
        student_grades[key] = "Fail"

for key in student_grades:
    print(f"{key} has written the exam with grade: {student_grades[key]}")