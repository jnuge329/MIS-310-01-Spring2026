#This file is my first project in my Midterm assignment.
# In[1]:
#Jeremiah Nugent- Midterm .py file
# PROJECT 1
from tkinter import *

def calculate_average_and_grade(scores):
    """User-defined function: calculates average and returns letter grade."""
    if not scores:
        return 0, "No scores entered"
    total = 0
    for score in scores: 
        total += score
    avg = total / len(scores)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return avg, grade

# GUI Setup
root = Tk()
root.title("Student Grade Tracker")
root.geometry("500x450")
root.resizable(0, 0)
root.configure(bg="#E6F3FF")

# Labels
title_label = Label(root, text="Student Letter Grade Calculator", font=("Arial", 16, "bold"), bg="#E6F3FF")
title_label.pack(pady=10)

Label(root, text="Enter up to 4 test scores (0-100):", font=("Arial", 10), bg="#E6F3FF").pack(pady=5)

# Entry widgets
score1_entry = Entry(root, width=10, font=("Arial", 12))
score1_entry.pack(pady=5)

score2_entry = Entry(root, width=10, font=("Arial", 12))
score2_entry.pack(pady=5)

score3_entry = Entry(root, width=10, font=("Arial", 12))
score3_entry.pack(pady=5)

score4_entry = Entry(root, width=10, font=("Arial", 12))
score4_entry.pack(pady=5)

scores_list = []

# Output label area
output_label = Label(root, text="Results will appear here", font=("Arial", 12), bg="#E6F3FF", justify="left", wraplength=450)
output_label.pack(pady=20)

# Button functions
def add_scores():
    """Collect scores from entries, add to list (with validation)."""
    global scores_list
    entries = [score1_entry, score2_entry, score3_entry, score4_entry]
    new_scores = []
    for entry in entries:
        try:
            val = float(entry.get().strip())
            if 0 <= val <= 100:
                new_scores.append(val)
            else:
                output_label.config(text="Error: Scores must be 0-100")
                return
        except ValueError:
            if entry.get().strip(): 
                output_label.config(text="Error: Enter valid numbers")
                return
    
    scores_list.extend(new_scores)
    output_label.config(text=f"Scores added: {scores_list}\n(Click Calculate for grade)")

def calculate():
    """Calculate average + letter grade using the user-defined function."""
    avg, grade = calculate_average_and_grade(scores_list)
    output_label.config(
        text=f"Scores: {scores_list}\n"
             f"Average: {avg:.2f}\n"
             f"Letter Grade: {grade}\n\n"
             f"{'Excellent!' if grade == 'A' else 'Good job!' if grade == 'B' else 'Keep working!' if grade in ['C','D'] else 'Need improvement'}"
    )

def clear_all():
    """Clear scores list and reset GUI."""
    global scores_list
    scores_list = []
    for entry in [score1_entry, score2_entry, score3_entry, score4_entry]:
        entry.delete(0, END)
    output_label.config(text="Results cleared - enter new scores")
    
# 3 Buttons included
add_btn = Button(root, text="Add Scores to List", command=add_scores, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=20)
add_btn.pack(pady=8)

calc_btn = Button(root, text="Calculate Average & Grade", command=calculate, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=20)
calc_btn.pack(pady=8)

clear_btn = Button(root, text="Clear All", command=clear_all, bg="#FF5722", fg="white", font=("Arial", 10, "bold"), width=20)
clear_btn.pack(pady=8)

root.mainloop()
