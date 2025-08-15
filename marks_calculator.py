# 🎓 Student Marks Calculator
# Author: Alisoju Sirichandana

# Get number of subjects
num_subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(num_subjects):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

# Calculate total and average
total = sum(marks)
average = total / num_subjects

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

# Display results
print("\n--- Student Result ---")
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
