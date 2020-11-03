import tkinter as tk
from tkinter import simpledialog

MODES = [
        ("White", "white"),
        ("Red", "red"),
        ("Green", "green"),
        ("Blue", "blue"),
        ("Black", "black"),
    ]

class GradientDialogue(tk.simpledialog.Dialog):
    """
    Dialogue window to choose settings for gradient
    """
    def body(self, master):
        self.v = tk.StringVar(master, "white")
        self.w = tk.StringVar(master, "white")
        self.y = tk.BooleanVar(master, True)

        tk.Label(master, text="Left color").grid(column=0, row=0)
        row = 1
        for text, mode in MODES:
            b = tk.Radiobutton(master, text=text, variable=self.v, value=mode)
            b.grid(column=0, row=row, sticky=tk.W, padx=10)
            row += 1

        tk.Label(master, text="Right color").grid(column=1, row=0)
        row = 1
        for text, mode in MODES:
            b = tk.Radiobutton(master, text=text, variable=self.w, value=mode)
            b.grid(column=1,row=row, sticky=tk.W, padx=10)
            row += 1

        tk.Label(master, text="Gradient Direction").grid(row=6)
        r1 = tk.Radiobutton(master, text="Horizontal", variable=self.y, value=True)
        r1.grid(column=0, row=7 )
        r1 = tk.Radiobutton(master, text="Vertical", variable=self.y, value=False)
        r1.grid(column=1, row=7)

        self.selection1 = None
        self.selection2 = None
        self.horizontal = True

    def apply(self):
        self.selection1, self.selection2, self.horizontal = self.v.get(), self.w.get(), self.y.get()