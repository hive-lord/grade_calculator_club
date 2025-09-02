# # Grade Calculator (Club Project)

This is a simple **Python grade calculator** developed as part of a club project.  
It takes marks for 5 subjects, validates the inputs, and provides options to calculate the **sum, average, and grades**.

---

## Features
- Input validation (marks must be between 0 and 100).
- Calculates **total sum** of marks.
- Calculates **average score**.
- Assigns **grades** based on the following logic:
  - A → 90 and above
  - B → 75–89
  - C → 50–74
  - F → Below 50
- Interactive menu system for easy use.

---

## Code Structure
- **`grade_all(d)`** → Assigns grades for each subject.
- **`sums(l)`** → Calculates and prints the total.
- **`average(l)`** → Calculates and prints the average.

---

## How It Works
1. User is prompted to enter marks for 5 subjects.  
2. Program ensures only valid marks (0–100) are accepted.  
3. After input, a menu is shown:
   - `1` → Calculate average  
   - `2` → Calculate sum  
   - `3` → Get grade list  
   - `4` → Exit  

---

## Why This Project
From my perspective, this project was a great way to learn **modular programming, input validation, and user interaction in Python**.  
It was built for a **club project** to demonstrate how simple programs can help analyze performance in education, while also showcasing clean and structured code practices.

---

## Run the Program
```bash
python grade_calculator.py
