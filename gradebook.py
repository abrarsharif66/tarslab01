names = ["Riya", "Ali", "Priya", "Rahul", "Sneha"]
marks = [92, 74, 88, 55, 97]

def get_grade(m):
    if m >= 90: return "A"
    elif m >= 80: return "B"
    elif m >= 50: return "C"
    else: return "F"

print("====== Grade Book ======")
total = 0
for i in range(len(names)):
    grade = get_grade(marks[i])
    print(f"{names[i]:<8} | {marks[i]:>3}/100 | {grade}")
    total = total + marks[i]

average = total / len(marks)
best_i  = marks.index(max(marks))
worst_i = marks.index(min(marks))

print(f"\nAverage : {average:.1f}")
print(f"Best    : {names[best_i]} ({marks[best_i]})")
print(f"Lowest  : {names[worst_i]} ({marks[worst_i]})")