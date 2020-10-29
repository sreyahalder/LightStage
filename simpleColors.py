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
        self.v = tk.StringVar(master, "white")

        for text, mode in MODES:
            b = tk.Radiobutton(master, text=text, variable=self.v, value=mode)
            b.pack(anchor=tk.W)

        self.selection = None

    def apply(self):
        self.selection = self.v.get()