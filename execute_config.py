import random
from createGradient import create_gradient

random.seed(1)

def delete(item, canvas):
    print("Deleting item ", item, "...")
    canvas.delete(item)

def set_param(param, root):
    """
    Check if we need to set random parameters
    """
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = random.randint(0, width) if param[0] == 'rand' else param[0]
    y = random.randint(0, height) if param[1] == 'rand' else param[1]
    w = random.randint(x, width) if param[2] == 'rand' else param[2]
    h = random.randint(y, height) if param[3] == 'rand' else param[3]
    color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) if param[4] == 'rand' else param[4]
    return w, h, x, y, color

def create_shape(canvas, type, w, h, x, y, color, param):
    if type == 'r':
        shape = canvas.create_rectangle(w, h, x, y, fill=color, tags="R")
    elif type == 'c':
        shape = canvas.create_oval(w, h, x, y, fill=color, tags="C")
    if len(param) > 6:
        canvas.after(int(param[6]), delete, shape, canvas)

def parse_config(config, canvas, root):
    lines = config.splitlines()
    for line in lines:
        type = line[0].lower()
        param = line[1:].split()
        if type == "g":
            color1, color2 = param[0], param[1]
            horizontal = True if param[2].lower() == "h" else False
            if len(param) == 3:
                create_gradient(root, canvas, horizontal, color1, color2)
            elif len(param) == 4:
                canvas.after(param[3], create_gradient, root, canvas, horizontal, color1, color2)
            elif len(param) == 5:
                canvas.after(param[3], create_gradient, root, canvas, horizontal, color1, color2)
                canvas.after(int(param[3]) + int(param[4]), delete, "gradient", canvas)
            continue

        w, h, x, y, color = set_param(param, root)

        if len(param) == 5:
            create_shape(canvas, type, w, h, x, y, color, param)
        elif len(param) > 5:
            canvas.after(param[5], create_shape, canvas, type, w, h, x, y, color, param)