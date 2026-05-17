import os
import tkinter as tk

DATA_FILE = "users.txt"

# Read saved username and password pairs from a file.
def read_file():
    users = {}
    if not os.path.exists(DATA_FILE):
        return users

    with open(DATA_FILE, "r", encoding="utf-8") as data:
        for line in data:
            line = line.strip()
            if not line or ":" not in line:
                continue
            username, password = line.split(":", 1)
            users[username] = password

    return users

# Write all username/password pairs back to the file.
def write_file(users):
    with open(DATA_FILE, "w", encoding="utf-8") as data:
        for username, password in users.items():
            data.write(f"{username}:{password}\n")

# Try to log in with the entered username and password.
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        message_label.config(text="Please enter both username and password.", fg="red")
        return

    users = read_file()
    if username in users and users[username] == password:
        message_label.config(text="Login successful! Welcome back.", fg="green")
    else:
        message_label.config(text="Login failed. Check username/password.", fg="red")

# Create a new account if the username is not already taken.
def signup():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        message_label.config(text="Please enter both username and password.", fg="red")
        return

    users = read_file()
    if username in users:
        message_label.config(text="Username already exists. Choose another.", fg="red")
        return

    users[username] = password
    write_file(users)
    message_label.config(text="Signup successful! You can now log in.", fg="green")

# Set up the Tkinter UI elements.
def main():
    global entry_username, entry_password, message_label

    root.title("Login System")
    root.geometry("320x220")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=16, pady=16)
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Username:", anchor="w").grid(row=0, column=0, sticky="w")
    entry_username = tk.Entry(frame, width=30)
    entry_username.grid(row=0, column=1, pady=8)

    tk.Label(frame, text="Password:", anchor="w").grid(row=1, column=0, sticky="w")
    entry_password = tk.Entry(frame, width=30, show="*")
    entry_password.grid(row=1, column=1, pady=8)

    login_button = tk.Button(frame, text="Login", width=12, command=login)
    login_button.grid(row=2, column=0, pady=12)

    signup_button = tk.Button(frame, text="Signup", width=12, command=signup)
    signup_button.grid(row=2, column=1, pady=12)

    message_label = tk.Label(frame, text="", fg="blue")
    message_label.grid(row=3, column=0, columnspan=2, pady=8)


root = tk.Tk()
main()
root.mainloop()