import pymysql
from tkinter import *
from tkinter import messagebox

# MySQL connection config
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root123;'
DB_NAME = 'university_db'

def connect_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def register():
    first = first_name.get()
    last = last_name.get()
    email_val = email.get()
    pwd = password.get()

    if not (first and last and email_val and pwd):
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
            (first, last, email_val, pwd)
        )
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except pymysql.err.IntegrityError:
        messagebox.showerror("Error", "Email already registered.")
    finally:
        conn.close()

def login():
    email_val = login_email.get()
    pwd = login_password.get()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE email=%s AND password=%s", (email_val, pwd))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login Success", f"Welcome {result[1]}!")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

def update():
    email_val = manage_email.get()
    new_first = new_first_name.get()
    new_pwd = new_password.get()

    if not email_val:
        messagebox.showwarning("Input Error", "Email is required to identify the account.")
        return

    if not new_first and not new_pwd:
        messagebox.showwarning("Input Error", "At least one field to update must be filled.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    if new_first:
        cursor.execute("UPDATE students SET first_name=%s WHERE email=%s", (new_first, email_val))
    if new_pwd:
        cursor.execute("UPDATE students SET password=%s WHERE email=%s", (new_pwd, email_val))

    conn.commit()
    conn.close()
    messagebox.showinfo("Update Success", "Account updated successfully!")

def delete():
    email_val = manage_email.get()
    if not email_val:
        messagebox.showwarning("Input Error", "Email is required to delete account.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE email=%s", (email_val,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Delete Success", "Account deleted successfully!")

# GUI
root = Tk()
root.title("Student Registration System")
root.geometry("400x650")

# Register Section
Label(root, text="Register", font=('Helvetica', 14, 'bold')).pack(pady=10)
Label(root, text="First Name").pack()
first_name = Entry(root)
first_name.pack()

Label(root, text="Last Name").pack()
last_name = Entry(root)
last_name.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Button(
    root,
    text="Register",
    command=register,
    bg="orange",
    fg="black",
    activebackground="orange",
    activeforeground="black"
).pack(pady=10)

# Divider
Label(root, text="").pack()

# Login Section
Label(root, text="Login", font=('Helvetica', 14, 'bold')).pack(pady=10)
Label(root, text="Email").pack()
login_email = Entry(root)
login_email.pack()

Label(root, text="Password").pack()
login_password = Entry(root, show="*")
login_password.pack()

Button(
    root,
    text="Login",
    command=login,
    bg="orange",
    fg="black",
    activebackground="orange",
    activeforeground="black"
).pack(pady=10)

# Divider
Label(root, text="").pack()

# Manage Account Section
Label(root, text="Manage Account", font=('Helvetica', 14, 'bold')).pack(pady=10)

Label(root, text="Your Email").pack()
manage_email = Entry(root)
manage_email.pack()

Label(root, text="New First Name (optional)").pack()
new_first_name = Entry(root)
new_first_name.pack()

Label(root, text="New Password (optional)").pack()
new_password = Entry(root, show="*")
new_password.pack()

Button(
    root,
    text="Update",
    command=update,
    bg="orange",
    fg="black",
    activebackground="orange",
    activeforeground="black"
).pack(pady=5)

Button(
    root,
    text="Delete",
    command=delete,
    bg="orange",
    fg="black",
    activebackground="orange",
    activeforeground="black"
).pack(pady=5)

root.mainloop()
