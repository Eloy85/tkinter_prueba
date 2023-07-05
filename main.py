import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            age = age_spinbox.get()
            title = title_combobox.get()
            nationality = nationality_combobox.get()
            # Courses info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print(f"First name: {firstname} - Last name: {lastname}")
            print(f"Age: {age} - Title: {title}")
            print(f"Nationality: {nationality}")
            print(f"Registration status: {registration_status}")
            print(f"Number of courses: {numcourses}")
            print(f"Number of semesters: {numsemesters}")
            print("--------------------------------------------------------------")

            # Create table
            conn = sqlite3.connect("database.db")
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data (firstname TEXT, lastname TEXT, age INT, title TEXT, nationality TEXT, registration_status TEXT, num_courses INT, num_semesters INT)
            '''
            conn.execute(table_create_query)

            # Insert data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, age, title, nationality, registration_status, num_courses, num_semesters)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            data_insert_tuple = (firstname, lastname, age, title, nationality, registration_status, numcourses, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()


        else:
            messagebox.showwarning("Error", "Please fill in all fields")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()

window.title("Data entry form")

frame = tkinter.Frame(window)
frame.pack()

# User info frame
user_info_frame = tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Ms."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Argentina", "Brasil", "Chile", "Paraguay", "Uruguay"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration status")

reg_status_var = tkinter.StringVar(value="Not registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently registered", variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Button

button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()