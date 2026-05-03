#This file is my second project (and part 1 of ) in my Midterm assignment.
# Jeremiah Nugent - Midterm
#Project 2 Part 1

from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import os

#Window Setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("580x560")
root.resizable(0, 0)
root.configure(bg='light blue')

#Inserting logo
logo_path = 'CCSULogomidterm.png'

if os.path.exists(logo_path):
    try:
        img = Image.open(logo_path).convert("RGBA")
        img = img.resize((160, 160), Image.Resampling.LANCZOS)


        datas = img.getdata()
        new_data = []
        for item in datas:

            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)

        logo_photo = ImageTk.PhotoImage(img)
        logo_label = Label(root, image=logo_photo, bg='light blue')
        logo_label.image = logo_photo
        logo_label.place(x=210, y=15)

    except Exception as e:
        print("Error loading logo:", e)

        Label(root, text="CCSU", font=("Arial", 40, "bold"), bg='light blue', fg="#003087").place(x=220, y=40)
else:
    print(f"Logo file not found: {logo_path}")
    Label(root, text="CCSU", font=("Arial", 40, "bold"), bg='light blue', fg="#003087").place(x=220, y=40)


Label(root, text="Central Connecticut State University",
      font=("Arial", 13, "bold"), bg='light blue', fg="#003087").place(x=145, y=185)

#Loading the CSV
try:
    data = pd.read_csv("examfile.csv")
except FileNotFoundError:
    data = pd.DataFrame()
    print("examfile.csv not found in the project folder.")

#Output Area
output_label = Label(root, justify="left", bg="white", anchor="nw",
                     font=("Arial", 10), relief="solid", bd=2,
                     width=68, height=17, padx=12, pady=10)
output_label.place(x=28, y=225)

#Button Functions
def show_calendar():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found in the project folder.")
        return
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected = df[~df['CalendarDate'].isnull()]
    output_label.config(text=selected.to_string(index=False))


def show_building():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found in the project folder.")
        return
    df = pd.DataFrame(data, columns=['Buildings'])
    selected = df[~df['Buildings'].isnull()]
    output_label.config(text=selected.to_string(index=False))


def show_faculty():
    if data.empty:
        output_label.config(text="Error: examfile.csv not found in the project folder.")
        return
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected = df[~df['FacultyName'].isnull()]
    output_label.config(text=selected.to_string(index=False))


#Buttons included
Button(root, text='Calendar', command=show_calendar, bg="light green",
       font=("Arial", 10, "bold"), width=13).place(x=65, y=205)

Button(root, text='Buildings', command=show_building, bg="light green",
       font=("Arial", 10, "bold"), width=13).place(x=225, y=205)

Button(root, text='Faculty', command=show_faculty, bg="light green",
       font=("Arial", 10, "bold"), width=13).place(x=385, y=205)

root.mainloop()
