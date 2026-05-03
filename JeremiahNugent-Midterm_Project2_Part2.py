# Jeremiah Nugent - Midterm
#Project 2 Part 2 (Enhanced)

from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import os

#Window Setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("620x620")
root.resizable(0, 0)
root.configure(bg='#E6F0FA')

#Inserting CCSU Logo
logo_path = 'CCSULogomidterm.png'

if os.path.exists(logo_path):
    try:
        img = Image.open(logo_path).convert("RGBA")
        img = img.resize((155, 155), Image.Resampling.LANCZOS)

        datas = img.getdata()
        new_data = []
        for item in datas:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        img.putdata(new_data)

        logo_photo = ImageTk.PhotoImage(img)
        logo_label = Label(root, image=logo_photo, bg='#E6F0FA')
        logo_label.image = logo_photo
        logo_label.place(x=232, y=15)
    except:
        Label(root, text="CCSU", font=("Arial", 38, "bold"), bg='#E6F0FA', fg="#003087").place(x=245, y=30)
else:
    Label(root, text="CCSU", font=("Arial", 38, "bold"), bg='#E6F0FA', fg="#003087").place(x=245, y=30)

#Inserting University label
Label(root, text="Central Connecticut State University",
      font=("Arial", 13, "bold"), bg='#E6F0FA', fg="#003087").place(x=165, y=185)

#Loading CSV
try:
    data = pd.read_csv("examfile.csv")
except FileNotFoundError:
    data = pd.DataFrame()

#Output Labels
output_label = Label(root, justify="left", bg="white", anchor="nw",
                     font=("Arial", 10), relief="solid", bd=2,
                     width=72, height=18, padx=15, pady=12)
output_label.place(x=35, y=280)


#Button Functions

# Original functions
def show_calendar():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found.")
        return
    df = pd.DataFrame(data, columns=['CalendarDate'])
    output_label.config(text=df[~df['CalendarDate'].isnull()].to_string(index=False))


def show_building():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found.")
        return
    df = pd.DataFrame(data, columns=['Buildings'])
    output_label.config(text=df[~df['Buildings'].isnull()].to_string(index=False))


def show_faculty():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found.")
        return
    df = pd.DataFrame(data, columns=['FacultyName'])
    output_label.config(text=df[~df['FacultyName'].isnull()].to_string(index=False))


# New buttons added
def show_school_of_business():
    text = """School of Business Majors / Programs:

• Accounting
• Finance
• Management & Organization
• Marketing
• Management Information Systems (MIS)
• Business Analytics"""
    output_label.config(text=text)


def show_mis_department():
    text = """MIS Department Courses:

• Introduction to MIS
• Database Management Systems
• Systems Analysis & Design
• Business Analytics / Data Visualization
• Network and Information Security
• Project Management
• Contemporary Business Applications Development"""
    output_label.config(text=text)


#Buttons

#Original 3 buttons
Button(root, text='Calendar', command=show_calendar, bg="#90EE90",
       font=("Arial", 10, "bold"), width=13).place(x=50, y=225)

Button(root, text='Buildings', command=show_building, bg="#90EE90",
       font=("Arial", 10, "bold"), width=13).place(x=210, y=225)

Button(root, text='Faculty', command=show_faculty, bg="#90EE90",
       font=("Arial", 10, "bold"), width=13).place(x=370, y=225)

#2 New Buttons
Button(root, text='School of Business', command=show_school_of_business, bg="#90EE90",
       font=("Arial", 10, "bold"), width=18).place(x=80, y=260)

Button(root, text='MIS Department', command=show_mis_department, bg="#90EE90",
       font=("Arial", 10, "bold"), width=18).place(x=340, y=260)

root.mainloop()
