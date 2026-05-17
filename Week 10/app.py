import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "users.txt"


# ---------------- FILE HANDLING ----------------
def read_file():
    users = {}
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(",")
                    users[username] = password
    except FileNotFoundError:
        pass
    return users

    return users

def write_file(username, password):
    with open(FILE_NAME, "a") as f:
        f.write(f"{username},{password}\n")


# ---------------- LOGIN FUNCTION ----------------
def login():
    username = entry_user.get()
    password = entry_pass.get()

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful!")
        main_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password")


# ---------------- SIGNUP FUNCTION ----------------
def signup():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Fields cannot be empty")
        return

    users = read_file()

    if username in users:
        messagebox.showerror("Error", "User already exists")
    else:
        write_file(username, password)
        messagebox.showinfo("Success", "Account created!")


# ---------------- MAIN SCREEN AFTER LOGIN ----------------
def main_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome!", font=("Arial", 20)).pack(pady=30)
    tk.Label(root, text="You are logged in.", font=("Arial", 14)).pack()


# ---------------- MAIN GUI ----------------
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")


tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()


tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Signup", command=signup).pack(pady=5)


root.mainloop()
print("Hello, World!")