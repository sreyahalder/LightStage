import tkinter as tk
from tkinter import simpledialog

MODES = [
        ("White", "white"),
        ("Red", "red"),
        ("Green", "green"),
        ("Blue", "blue"),
    ]

class MyDialog(tk.simpledialog.Dialog):
    """
    Dialogue window to choose color of sequence rectangle
    """
    def body(self, master):
        self.parent = master
        e1_var = tk.IntVar(value=2)
        e2_var = tk.IntVar(value=2)
        e3_var = tk.IntVar(value=200)

        l1 = tk.Label(master, width=22, text="Rows (1-100)").pack()
        self.e1 = tk.Entry(master, textvariable=e1_var)
        self.e1.pack()
        self.rows = 2
        l2 = tk.Label(master, width=22, text="Columns (1-100)").pack()
        self.e2 = tk.Entry(master, textvariable=e2_var)
        self.e2.pack()
        self.cols = 2
        l3 = tk.Label(master, width=22, text="Time (ms)").pack()
        self.e3 = tk.Entry(master, textvariable=e3_var)
        self.e3.pack()
        self.time = 100

        l4 = tk.Label(master, width=22, text="Color").pack()
        self.v = tk.StringVar(master, "white")
        for text, mode in MODES:
            b = tk.Radiobutton(master, text=text, variable=self.v, value=mode)
            b.pack(anchor=tk.W, padx=40)
        self.color = "white"

        self.w = master.winfo_screenwidth() / self.cols
        self.h = master.winfo_screenheight() / self.rows

        self.mySubmitButton = tk.Button(master, text='Update Rectangle', command=self.update)
        self.mySubmitButton.pack(pady=5)

        self.canv = tk.Canvas(master, highlightthickness=0, height=self.h + 5, width=self.w + 5)
        self.canv.pack()
        self.rect = self.canv.create_rectangle(5, 5, self.w, self.h, fill="white", tags="R")

        self.cont = False


    def apply(self, *args):
        self.color = self.v.get()
        self.rows = self.e1.get()
        self.cols = self.e2.get()
        self.time = self.e3.get()
        self.w = self.parent.winfo_screenwidth() / int(self.rows)
        self.h = self.parent.winfo_screenheight() / int(self.cols)
        self.cont = True

    def update(self):
        self.w = self.parent.winfo_screenwidth() / int(self.e2.get())
        self.h = self.parent.winfo_screenheight() / int(self.e1.get())
        self.color = self.v.get()
        self.canv.itemconfig(self.rect, fill=self.color)
        self.canv.coords(self.rect, 5, 5, self.w, self.h)
