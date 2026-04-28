import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of students
n = 50

# Generate data
data = {
    "StudentID": range(1, n+1),
    "Marks": np.random.randint(40, 100, n),        # Marks between 40–100
    "Attendance": np.random.randint(60, 100, n),   # Attendance between 60–100%
    "StudyHours": np.random.randint(1, 10, n)      # Study hours between 1–9
}

df = pd.DataFrame(data)

# Efficiency = Marks / StudyHours
df["Efficiency"] = (df["Marks"] / df["StudyHours"]).round(2)

# Assign Grades
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(assign_grade)

# Save to CSV
df.to_csv("students.csv", index=False)

print("✅ Dataset generated successfully as students.csv")
print(df.head())