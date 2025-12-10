scores = [95, 45, 78, 82, 60]
results = []

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for score in scores:
    grade = get_grade(score)
    results.append((grade))

print("Результати студентів:")
print(results)