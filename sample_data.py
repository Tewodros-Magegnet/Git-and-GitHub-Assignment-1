print('This is sample data for Assignment 1')
def get_letter_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 85:
        return "A"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Example usage:
student_score = 88
grade = get_letter_grade(student_score)
print(f"Score: {student_score} | Grade: {grade}")
