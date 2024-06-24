import tkinter as tk
from random import *

signs = [
    "0123456789",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "!#$%&*+-=?@^_?",
]


def get_password():
    password = ""

    length = len_password.get()
    if not (length.isdigit()):
        pole_of_password.delete(0, tk.END)
        pole_of_password.insert(0, "Wrong length")
    else:
        length = int(length)
        for i in range(length):
            rand_lst = signs[randint(0, 3)]
            rand_sym = rand_lst[randint(0, len(rand_lst) - 1)]
            password += rand_sym
        pole_of_password.delete(0, tk.END)
        pole_of_password.insert(0, password)


root = tk.Tk()
root.geometry("400x200+500+100")
root.title("Password generator by GonzoMonk")

pole_of_password = tk.Entry(root)
len_password = tk.Entry(root)
gen_btn = tk.Button(root, text="Generate", command=get_password)
label1 = tk.Label(root, text="Symbols in password:", font=("Arial", 11))
label2 = tk.Label(root, text="Password generator", font=("Arial", 22))

pole_of_password.place(x=50, y=50, height=20, width=300)
label1.place(x=50, y=100)
label2.place(x=65, y=5)
len_password.place(x=200, y=100, width=30)
gen_btn.place(x=300, y=150)


root.mainloop()
