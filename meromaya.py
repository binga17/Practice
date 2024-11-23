import tkinter as tk
from tkinter import simpledialog, messagebox
def get_password():
    password = simpledialog.askstring('Password Input','Enter your password:', show = '*')
    if password is not None:
        messagebox.showinfo('Password Entered', f'Your password is: {password}')
    else:
        message.showinfo('Password Input', 'No password entered.')
root = tk.Tk()
root.withdraw()
get_password()
root.destroy()