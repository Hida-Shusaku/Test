import zipfile
import re
import json
import tkinter as tk
import time

root = tk.Tk()
root.title('Image')
root.geometry("800x700")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

def create_image(a):
    lines=[]
    lines.append(canvas.create_line(a[0]/2, a[1]/2, a[45]/2, a[46]/2, tag = "image"))   #0-15
    lines.append(canvas.create_line(a[0]/2, a[1]/2, a[48]/2, a[49]/2, tag = "image"))   #0-16
    lines.append(canvas.create_line(a[45]/2, a[46]/2, a[51]/2, a[52]/2, tag = "image"))   #15-17
    lines.append(canvas.create_line(a[48]/2, a[49]/2, a[54]/2, a[55]/2, tag = "image"))   #16-18
    lines.append(canvas.create_line(a[3]/2, a[4]/2, a[0]/2, a[1]/2, tag = "image"))   #1-0
    lines.append(canvas.create_line(a[3]/2, a[4]/2, a[6]/2, a[7]/2, tag = "image"))   #1-2
    lines.append(canvas.create_line(a[3]/2, a[4]/2, a[15]/2, a[16]/2, tag = "image")) #1-5
    lines.append(canvas.create_line(a[3]/2, a[4]/2, a[24]/2, a[25]/2, tag = "image")) #1-8
    lines.append(canvas.create_line(a[6]/2, a[7]/2, a[9]/2, a[10]/2, tag = "image"))  #2-3
    lines.append(canvas.create_line(a[9]/2, a[10]/2, a[12]/2, a[13]/2, tag = "image"))    #3-4
    lines.append(canvas.create_line(a[15]/2, a[16]/2, a[18]/2, a[19]/2, tag = "image"))   #5-6
    lines.append(canvas.create_line(a[18]/2, a[19]/2, a[21]/2, a[22]/2, tag = "image"))   #6-7
    lines.append(canvas.create_line(a[24]/2, a[25]/2, a[27]/2, a[28]/2, tag = "image"))   #8-9
    lines.append(canvas.create_line(a[24]/2, a[25]/2, a[36]/2, a[37]/2, tag = "image"))   #8-12
    lines.append(canvas.create_line(a[27]/2, a[28]/2, a[30]/2, a[31]/2, tag = "image"))   #9-10
    lines.append(canvas.create_line(a[30]/2, a[31]/2, a[33]/2, a[34]/2, tag = "image"))   #10-11
    lines.append(canvas.create_line(a[33]/2, a[34]/2, a[66]/2, a[67]/2, tag = "image"))   #11-22
    lines.append(canvas.create_line(a[33]/2, a[34]/2, a[72]/2, a[73]/2, tag = "image"))   #11-24
    lines.append(canvas.create_line(a[66]/2, a[67]/2, a[69]/2, a[70]/2, tag = "image"))   #22-23
    lines.append(canvas.create_line(a[36]/2, a[37]/2, a[39]/2, a[40]/2, tag = "image"))   #12-13
    lines.append(canvas.create_line(a[39]/2, a[40]/2, a[42]/2, a[43]/2, tag = "image"))   #13-14
    lines.append(canvas.create_line(a[42]/2, a[43]/2, a[57]/2, a[58]/2, tag = "image"))   #14-19
    lines.append(canvas.create_line(a[42]/2, a[43]/2, a[63]/2, a[64]/2, tag = "image"))   #14-21
    lines.append(canvas.create_line(a[57]/2, a[58]/2, a[60]/2, a[61]/2, tag = "image"))   #19-20

    for line in lines:
        coordinates = canvas.coords(line)
        if 0 in coordinates:
            canvas.delete(line)


with zipfile.ZipFile("kabeposter.zip", "r") as zf:
    b=[]
    for i in zf.namelist():
        try:
            name = re.findall(r'_(.*?)_', i)
            n=int(name[0])
            
            with zf.open(i) as f:
                dict = json.load(f)
                a = dict["people"]
                for j in a:
                    b.append(j["pose_keypoints_2d"])
        except:
            pass


for i in range(int(len(b)/2)):
    root.update()
    canvas.delete("all")
    create_image(b[2*i])
    create_image(b[2*i+1])
    time.sleep(0.05)

root.mainloop()