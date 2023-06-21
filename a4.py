import tkinter as tk

root = tk.Tk()
root.title('Image')
root.geometry("400x400")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_oval(100, 50, 150, 100)   #頭
canvas.create_line(125, 100, 125, 160)  #胴体
canvas.create_line(125, 160, 80, 200)   #左足
canvas.create_line(125, 160, 170, 200)  #右足
canvas.create_line(125, 125, 80, 90)    #左手
canvas.create_line(125, 125, 170, 90)   #右手

root.mainloop()