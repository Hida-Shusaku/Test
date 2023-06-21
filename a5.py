import tkinter as tk

root = tk.Tk()
root.title('Image')
root.geometry("400x400")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

def create_image(x, y, w):
    canvas.create_oval(x, y, x+w, y+w, tag = "image")   #頭
    canvas.create_line(x+w/2, y+w, x+w/2, y+2*w, tag = "image")  #胴体
    canvas.create_line(x+w/2, y+2*w, x-x/5, 2*(y+w), tag = "image")   #左足
    canvas.create_line(x+w/2, y+2*w, x+w+x/5, 2*(y+w), tag = "image")  #右足
    canvas.create_line(x+w/2, y+w+w/2, x-x/5, y+w, tag = "image")    #左手
    canvas.create_line(x+w/2, y+w+w/2, x+w+x/5, y+w, tag = "image")   #右手

def move():
    canvas.move("image", 10, 0)
    canvas.after(100, move)

create_image(100, 50, 50)
move()


root.mainloop()