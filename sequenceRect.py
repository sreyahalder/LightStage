import tkinter as tk

class MyDialog(tk.simpledialog.Dialog):
    """
    Dialogue window to confirm size of rectangle for sequence
    """
    def __init__(self, parent, w, h, color):
        self.top = tk.Toplevel(parent)
        self.cont = False

        self.myLabel = tk.Label(self.top, text='Rectangle size')
        self.myLabel.pack()

        self.canv = tk.Canvas(self.top, highlightthickness=0, height=h+5, width=w+5)
        self.canv.pack()
        self.canv.create_rectangle(5, 5, w, h, fill=color, tags="R")

        self.mySubmitButton = tk.Button(self.top, text='OK', command=self.send)
        self.mySubmitButton.pack(pady=5)
        parent.wait_window(self.top)

    def send(self):
        self.cont = True
        self.top.destroy()