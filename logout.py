import tkinter as tk
from tkinter import messagebox

def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        root.destroy()  # Close the application
        # Alternatively, you could return to a login screen
        # login_screen()

root = tk.Tk()
root.title("Application with Logout")

# Create a logout button
logout_btn = tk.Button(root, text="Logout", command=logout, bg="red", fg="white")
logout_btn.pack(pady=20)

root.mainloop()