import tkinter as tk   # Py3
import random

dice = [1, 2, 3, 4, 5, 6]

def callback():
    label.configure(text=f"Wynik: {random.choice(dice)}")


root = tk.Tk()

root.title("Rzut kostką")

root.geometry("200x200")

button = tk.Button(root, text="Rzut kostką", width=10, height=2,background="grey",fg="blue", command=callback,)
label = tk.Label(root, text="Wynik: ")
label.grid(row=0, column=1)
button.grid(row=1, column=1)

root.mainloop()
