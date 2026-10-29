import tkinter as tk
from tkinter import ttk, messagebox
import csv


def check_phone(value):
    return value == "" or (value.isascii() and value.isdigit()
                           and len(value) <= 10)


def submit():
    name = name_entry.get().strip()
    div = div_entry.get().strip()
    roll = roll_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not all([name, div, roll, email, phone]):
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    if "@" not in email or not email.endswith(".com"):
        messagebox.showwarning(
            "Invalid Email", "Email must contain @ and end with .com."
        )
        return

    if len(phone) != 10:
        messagebox.showwarning(
            "Invalid Phone", "Phone number must have exactly 10 digits."
        )
        return

    with open("student.txt", "a", newline="") as file:
        csv.writer(file).writerow([name, div, roll, email, phone])

    messagebox.showinfo("Success", "Details saved successfully!")


def read():
    try:
        with open("student.txt", "r", newline="") as file:
            records = list(csv.reader(file))
    except FileNotFoundError:
        messagebox.showinfo("No Data", "Submit details first.")
        return

    window = tk.Toplevel(root)
    window.title("Student Records")

    columns = ("Name", "Division", "Roll No", "Email", "Phone")
    table = ttk.Treeview(window, columns=columns, show="headings")

    for column in columns:
        table.heading(column, text=column)
        table.column(column, width=150, anchor="center")

    table.column("Email", width=230)

    for record in records:
        if len(record) == 3:
            record += ["", ""]  
        if len(record) == 5:
            table.insert("", tk.END, values=record)

    table.pack(padx=10, pady=10)


root = tk.Tk()
root.title("Student Details")
root.geometry("350x430")

tk.Label(root, text="Student Name").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Division").pack(pady=5)
div_entry = tk.Entry(root)
div_entry.pack()

tk.Label(root, text="Roll No").pack(pady=5)
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Phone Number").pack(pady=5)
phone_validation = (root.register(check_phone), "%P")
phone_entry = tk.Entry(
    root,
    validate="key",
    validatecommand=phone_validation
)
phone_entry.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)
tk.Button(root, text="Read", command=read).pack()

root.mainloop()
