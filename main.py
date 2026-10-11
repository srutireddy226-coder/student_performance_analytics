import pandas as pd
import numpy as np

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"

def calculate_result(row, subjects):
    if all(row[subject] >= 35 for subject in subjects):
        return "Pass"
    return "Fail"

def main():
    df = pd.read_csv("students.csv")
    subjects = ["Python", "Mathematics", "AI"]

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1).round(2)
    df["Grade"] = df["Average"].apply(calculate_grade)
    df["Result"] = df.apply(lambda row: calculate_result(row, subjects), axis=1)

    print("\n===== STUDENT PERFORMANCE REPORT =====")
    print(df.to_string(index=False))

    print("\n===== CLASS STATISTICS =====")
    print("Total Students:", len(df))
    print("Class Average:", round(df["Average"].mean(), 2))
    print("Highest Average:", df["Average"].max())
    print("Lowest Average:", df["Average"].min())
    print("Students Passed:", (df["Result"] == "Pass").sum())
    print("Students Failed:", (df["Result"] == "Fail").sum())

    print("\n===== SUBJECT-WISE AVERAGES =====")
    for subject in subjects:
        print(f"{subject} Average: {np.mean(df[subject]):.2f}")

    print("\n===== TOP 5 STUDENTS =====")
    print(df.nlargest(5, "Average")[["Student_ID", "Name", "Average", "Grade"]].to_string(index=False))

    df.to_csv("student_performance_report.csv", index=False)
    print("\nFinal report saved as student_performance_report.csv")
    print("Project executed successfully!")

if __name__ == "__main__":
    main()
