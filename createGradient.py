def create_gradient(window, canvas, horizontal, color1, color2):
    canvas.delete("all")
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