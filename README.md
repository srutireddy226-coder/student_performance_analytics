# Student Performance Analytics System

A Python data-analysis mini project using **Pandas** and **NumPy** to summarize student performance.

## Features
- Reads student records from `students.csv`
- Calculates total and average marks across Python, Mathematics, and AI
- Assigns grades based on average marks
- Determines pass/fail (at least 35 in each listed subject)
- Displays class statistics and subject-wise averages
- Lists the top five students
- Exports results to `student_performance_report.csv`

## Requirements
- Python 3.9+
- pandas
- numpy

Install dependencies:
```bash
pip install pandas numpy
```

## Run the project
Keep `main.py` and `students.csv` in the same folder, then run:
```bash
python main.py
```

## Files
- `main.py` — main program
- `students.csv` — sample dataset with 20 student records
- `student_performance_report.csv` — generated after running the program
- `Student_Performance_Analytics_Documentation.pdf` — project documentation
- `Student_Performance_Analytics_Documentation.docx` — editable documentation

## Grading rules
- A+: average >= 90
- A: average >= 80
- B: average >= 70
- C: average >= 60
- D: average >= 50
- F: average < 50

A student passes when their marks are at least 35 in each of Python, Mathematics, and AI.

## Before submission
Replace the blank student details in the documentation, add screenshots of your actual output, and add your GitHub repository URL after uploading the files.
