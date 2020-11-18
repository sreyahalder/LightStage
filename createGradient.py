import cv2

def create_gradient(window, canvas, horizontal, color1, color2):
    width = window.winfo_width()
    height = window.winfo_height()
    limit = width if horizontal else height
    (r1, g1, b1) = window.winfo_rgb(color1)
    (r2, g2, b2) = window.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
        if horizontal:
            canvas.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        else:
            canvas.create_line(0, i, width, i, tags=("gradient",), fill=color)
    canvas.lower("gradient")

# Delete specific item
def delete(canvas, item):
    canvas.delete(item)

# Create rectangles for sequence
def create_rect(cam, canvas, sequence_time, x, y, w, h, color, img_count):
    canvas.delete("all")
    rect = canvas.create_rectangle(x, y, w, h, fill=color, tags="R", outline="")
    canvas.after(sequence_time//2, snapshot, cam, canvas, img_count)
    canvas.after(sequence_time, delete, canvas, rect)

    # Take snapshot
def snapshot(cam, canvas, img_count, horizontal = "H", color1="black", color2="black"):
    # Replace with your directory
    img_name = "/Users/halde/Documents/test_snapshots/{:04d}.png".format(img_count)
    ret, frame = cam.read()
    cv2.imwrite(img_name, frame)

    # Replace with your directory
    config = open("/Users/halde/Documents/test_snapshots/{:04d}.txt".format(img_count), "w")
    if canvas.find_withtag("gradient"):
        config.write("G " + color1 + " " + color2 + " ")
        if horizontal: config.write("H\n")
        else: config.write("V\n")
    else:
        items = canvas.find_all()
        for item in items:
            config.write(canvas.itemcget(item, "tags") + " " + str(canvas.bbox(item)[0]) + " "
                         + str(canvas.bbox(item)[1]) + " " + str(canvas.bbox(item)[2]) + " " +
                         str(canvas.bbox(item)[3]) + " " + canvas.itemcget(item, "fill") + "\n")
    config.close()
    img_count += 1

# Run sequence
def sequence(sequence_rows, sequence_columns, canvas, width, height, color, sequence_time, cam, img_count):
    time = 0
    y = 0
    for i in range(sequence_rows):
        x = 0
        for j in range(sequence_columns):
            canvas.after(time, create_rect, cam, canvas, sequence_time, x, y, x + width, y + height, color, img_count)
            time += sequence_time
            x += width
        y += height