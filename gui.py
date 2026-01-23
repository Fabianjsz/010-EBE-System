from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = Tk()
root.title("EBE-App")
root.geometry("700x500")
root.config(bg="lightgrey")


frm = tk.Frame(root)
frm.grid()

# Entry widgets
entry_vorname = tk.Entry(frm, width=30).grid(column=1, row=1)
entry_name = tk.Entry(frm, width=30).grid(column=1, row=2)
entry_adresse = tk.Entry(frm, width=30).grid(column=1, row=3)
entry_hausnummer = tk.Entry(frm, width=30).grid(column=1, row=4)
entry_ort = tk.Entry(frm, width=30).grid(column=1, row=5)



tk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


root.mainloop()