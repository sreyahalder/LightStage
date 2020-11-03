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
        e1_var = tk.IntVar()
        e2_var = tk.IntVar()
        e3_var = tk.IntVar()

        l1 = tk.Label(master, width=22, text="Rows (1-100)").pack()
        self.e1 = tk.Entry(master, textvariable=e1_var)
        self.e1.pack()
        self.rows = None
        l2 = tk.Label(master, width=22, text="Columns (1-100)").pack()
        self.e2 = tk.Entry(master, textvariable=e2_var)
        self.e2.pack()
        self.cols = None
        l3 = tk.Label(master, width=22, text="Time (ms)").pack()
        self.e3 = tk.Entry(master, textvariable=e3_var)
        self.e3.pack()
        self.time = None

        l4 = tk.Label(master, width=22, text="Color").pack()
        self.v = tk.StringVar(master, "white")
        for text, mode in MODES:
            b = tk.Radiobutton(master, text=text, variable=self.v, value=mode)
            b.pack(anchor=tk.W, padx=40)
        self.color = None

        e1_var.trace("w", self.update_rect)
        e2_var.trace("w", self.update_rect)
        self.v.trace("w", self.update_rect)

    def apply(self, *args):
        self.color = self.v.get()
        self.rows = self.e1.get()
        self.cols = self.e2.get()
        self.time = self.e3.get()

    def update_rect(self):
        pass
