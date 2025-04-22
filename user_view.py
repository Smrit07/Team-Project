import tkinter as tk
from tkinter import messagebox
from auth import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def login():
    username = username_entry.get()
    password = password_entry.get()
    role = authenticate(username, password)

    if role:
        user = get_user_details(username)
        login_win.destroy()  # Close login window after success
        if role == "admin":
            admin_dashboard(user)
        elif role == "student":
            student_dashboard(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def admin_dashboard(user):
    win = tk.Tk()
    win.title("Admin Dashboard")
    win.geometry("400x300")

    frame = tk.Frame(win, padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text=f"Welcome {user.full_name}", font=("Arial", 14)).pack(pady=10)

    def add_ui():
        def submit():
            u = u_entry.get()
            f = f_entry.get()
            p = p_entry.get()
            r = role_var.get()
            if not all([u, f, p]):
                messagebox.showerror("Input Error", "All fields are required.")
                return
            if add_user(u, f, p, r):
                messagebox.showinfo("Success", "User added!")
                add_win.destroy()
            else:
                messagebox.showerror("Failed", "User already exists.")

        add_win = tk.Toplevel(win)
        add_win.title("Add User")
        add_win.geometry("300x250")
        frame = tk.Frame(add_win, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text="Username").pack()
        u_entry = tk.Entry(frame)
        u_entry.pack()
        tk.Label(frame, text="Full Name").pack()
        f_entry = tk.Entry(frame)
        f_entry.pack()
        tk.Label(frame, text="Password").pack()
        p_entry = tk.Entry(frame, show="*")
        p_entry.pack()
        tk.Label(frame, text="Role").pack()
        role_var = tk.StringVar(value="student")
        tk.OptionMenu(frame, role_var, "admin", "student").pack()
        tk.Button(frame, text="Submit", command=submit).pack(pady=10)

    def delete_ui():
        def submit():
            u = entry.get()
            if delete_user(u):
                messagebox.showinfo("Deleted", "User deleted.")
                delete_win.destroy()
            else:
                messagebox.showerror("Error", "User not found.")

        delete_win = tk.Toplevel(win)
        delete_win.title("Delete User")
        delete_win.geometry("250x150")
        frame = tk.Frame(delete_win, padx=10, pady=10)
        frame.pack()
        tk.Label(frame, text="Username").pack()
        entry = tk.Entry(frame)
        entry.pack()
        tk.Button(frame, text="Delete", command=submit).pack(pady=10)

    tk.Button(frame, text="Add User", command=add_ui, width=20).pack(pady=5)
    tk.Button(frame, text="Delete User", command=delete_ui, width=20).pack(pady=5)

    win.mainloop()

def student_dashboard(user):
    win = tk.Tk()
    win.title("Student Dashboard")
    win.geometry("400x400")

    frame = tk.Frame(win, padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text=f"Welcome {user.full_name}", font=("Arial", 14)).pack(pady=10)

    def view_info():
        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)

        info_win = tk.Toplevel(win)
        info_win.title("Student Info")
        info_win.geometry("500x400")

        tk.Label(info_win, text=f"Name: {user.full_name}", font=("Arial", 12)).pack(pady=5)

        # Grades Section
        tk.Label(info_win, text="Grades:", font=("Arial", 10, "bold")).pack()

        fig, ax = plt.subplots(figsize=(5, 2))
        ax.bar(range(len(grades)), grades, tick_label=[f"Sub {i+1}" for i in range(len(grades))])
        ax.set_ylabel("Grade")
        ax.set_ylim(0, 100)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=info_win)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        # ECA Section
        tk.Label(info_win, text="Extra Curricular Activities:", font=("Arial", 10, "bold")).pack()
        for act in eca:
            tk.Label(info_win, text=f"- {act}").pack()

    def update_info():
        def submit():
            new_name = name_entry.get()
            if update_student_profile(user.username, new_name):
                messagebox.showinfo("Updated", "Profile updated.")
                update_win.destroy()

        update_win = tk.Toplevel(win)
        update_win.title("Update Info")
        update_win.geometry("300x150")
        frame = tk.Frame(update_win, padx=10, pady=10)
        frame.pack()
        tk.Label(frame, text="New Full Name").pack()
        name_entry = tk.Entry(frame)
        name_entry.insert(0, user.full_name)
        name_entry.pack()
        tk.Button(frame, text="Submit", command=submit).pack(pady=10)

    tk.Button(frame, text="View Info", command=view_info, width=20).pack(pady=5)
    tk.Button(frame, text="Update Info", command=update_info, width=20).pack(pady=5)

    win.mainloop()

def main():
    global username_entry, password_entry, login_win
    login_win = tk.Tk()
    login_win.title("SPMS Login")
    login_win.geometry("300x250")

    frame = tk.Frame(login_win, padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text="SPMS Login", font=("Arial", 14)).pack(pady=10)
    tk.Label(frame, text="Username").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)
    tk.Label(frame, text="Password").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)
    tk.Button(frame, text="Login", command=login, width=15).pack(pady=10)

    login_win.mainloop()

if __name__ == "__main__":
    main()
