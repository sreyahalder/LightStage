import cv2
import tkinter as tk
import tkinter.colorchooser
from tkinter.filedialog import askopenfile
from execute_config import parse_config
from tkinter import simpledialog
import simpleColors
import gradientColor
from createGradient import create_gradient
import sequenceRect

cam = cv2.VideoCapture(0)

class LightStage:
    def __init__(self):
        self.window = tk.Tk()
        # Set window to fullscreen
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        # Initialize Canvas
        self.x = self.y = 0
        self.window.configure(bg='black')
        self.canvas = tk.Canvas(self.window, bg='black', highlightthickness=0)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        # Variables to keep track of
        self.shape = "R"
        self.window.bind("r", self.draw_rect)
        self.window.bind("c", self.draw_circle)
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.curr_item = None

        # Right click menu
        self.m = tk.Menu(self.window, tearoff=0)
        self.m.add_command(label="Color", command=self.change_color)
        self.m.add_command(label="Delete", command=self.delete_item)
        self.canvas.bind("<ButtonPress-2>", self.popup)

        # General right click menu
        self.m2 = tk.Menu(self.window, tearoff=0)
        self.m2.add_command(label="Color All", command=self.color_all)
        self.m2.add_command(label="Delete All", command=self.delete_all)
        self.m2.add_command(label="Import Config", command=lambda: self.open_file())
        self.m2.add_command(label="Sequence", command=self.sequence)
        self.m2.add_command(label="Gradient", command=self.gradient)
        self.m2.add_command(label="Snapshot", command=self.snapshot)

        # Sequence options
        self.sequence_time = 50
        self.sequence_rows = 4
        self.sequence_columns = 4
        self.img_count = 0

        # Gradient
        self.m3 = tk.Menu(self.window, tearoff=0)
        self.m3.add_command(label="Delete Gradient", command=self.delete_gradient)
        self.m3.add_command(label="Snapshot", command=self.snapshot)
        self.color1 = "black"
        self.color2 = "black"
        self.horizontal = True

        # Pack
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    # Toggle draw rectangle
    def draw_rect(self, event):
        self.shape = "R"

    # Toggle draw circle
    def draw_circle(self, event):
        self.shape = "C"

    # Start dragging rectangle
    def on_mouse_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.shape == "R": self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill="white", tags="R")
        else: self.rect = self.canvas.create_oval(self.x, self.y, 1, 1, fill="white", tags="C")

    # Draw rectangle on mouse drag
    def on_mouse_drag(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_mouse_release(self, event):
        pass

    # Popup menus
    def popup(self, event):
        overlap = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if self.canvas.find_withtag("gradient"):
            try:
                self.m3.tk_popup(event.x_root, event.y_root)
            finally:
                self.m3.grab_release()
        elif len(overlap) > 0:
            self.curr_item = overlap[-1]
            try:
                self.m.tk_popup(event.x_root, event.y_root)
            finally:
                self.m.grab_release()
        else:
            try:
                self.m2.tk_popup(event.x_root, event.y_root)
            finally:
                self.m2.grab_release()

    # Delete current item
    def delete_item(self):
        self.canvas.delete(self.curr_item)
        print("Deleted item: ", self.curr_item)

    # Delete specific item
    def delete(self, item):
        self.canvas.delete(item)

    # Change color of current item
    def change_color(self):
        color = tk.colorchooser.askcolor()
        self.canvas.itemconfig(self.curr_item, fill=color[-1])
        print("Changed color of item: ", self.curr_item)

    def delete_all(self):
        self.canvas.delete("all")
        print("Deleted all")

    def color_all(self):
        color = tk.colorchooser.askcolor()
        self.canvas.itemconfig("all", fill=color[-1])
        print("Changed color for all")

    # Open and read config file
    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if file is not None:
            config = file.read()
            print(config)
            parse_config(config, self.canvas, self.window)

    # Create rectangles for sequence
    def create_rect(self, x, y, w, h, color):
        rect = self.canvas.create_rectangle(x, y, w, h, fill=color, tags="R")
        self.canvas.after(self.sequence_time//2, self.snapshot)
        self.canvas.after(self.sequence_time, self.delete, rect)

    # Take snapshot
    def snapshot(self):
        # Replace with your directory
        img_name = "/Users/halde/Documents/test_snapshots/{:04d}.png".format(self.img_count)
        ret, frame = cam.read()
        cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))

        # Replace with your directory
        config = open("/Users/halde/Documents/test_snapshots/{:04d}.txt".format(self.img_count), "w")
        if self.canvas.find_withtag("gradient"):
            config.write("G " + self.color1 + " " + self.color2 + " ")
            if self.horizontal: config.write("H\n")
            else: config.write("V\n")
        else:
            items = self.canvas.find_all()
            for item in items:
                config.write(self.canvas.itemcget(item, "tags") + " " + str(self.canvas.bbox(item)[0]) + " "
                         + str(self.canvas.bbox(item)[1]) + " " + str(self.canvas.bbox(item)[2]) + " " +
                         str(self.canvas.bbox(item)[3]) + " " + self.canvas.itemcget(item, "fill") + "\n")
        config.close()
        self.img_count += 1

    # Run sequence
    def sequence(self):
        self.sequence_rows = simpledialog.askinteger("Input", "Sequence rows? (0 - 100)",
                                                        parent=self.window, minvalue=0, maxvalue=100)
        if self.sequence_rows is None: return
        self.sequence_columns = simpledialog.askinteger("Input", "Sequence columns? (0 - 100)",
                                                     parent=self.window, minvalue=0, maxvalue=100)
        if self.sequence_columns is None: return
        self.sequence_time = simpledialog.askinteger("Input", "Sequence time? (ms)",
                                                        parent=self.window, minvalue=0)
        if self.sequence_time is None: return
        color = simpleColors.MyDialog(self.window).selection
        if color is None: return
        time = 0
        y = 0
        width = self.window.winfo_screenwidth() / self.sequence_columns
        height = self.window.winfo_screenheight() / self.sequence_rows

        cont = sequenceRect.MyDialog(self.window, width, height, color).cont
        if not cont: return

        for i in range(self.sequence_rows):
            x = 0
            for j in range(self.sequence_columns):
                self.canvas.after(time, self.create_rect, x, y, x + width, y + height, color)
                time += self.sequence_time
                x += width
            y += height

    # Draw gradient
    def gradient(self):
        gradient = gradientColor.GradientDialogue(self.window)
        self.color1, self.color2, self.horizontal = gradient.selection1, gradient.selection2, gradient.horizontal
        if self.color1 is None or self.color2 is None: return
        create_gradient(self.window, self.canvas, self.horizontal, self.color1, self.color2)

    def delete_gradient(self):
        self.canvas.delete("gradient")

if __name__ == '__main__':
    app = LightStage()