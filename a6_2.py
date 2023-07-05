import zipfile
import re
import json
import tkinter as tk


with zipfile.ZipFile("kabeposter.zip", "r") as zf:
    for i in zf.namelist():
        try:
            name = re.findall(r'_(.*?)_', i)
            n=int(name[0])
            if n==0:
                with zf.open(i) as f:
                    dict = json.load(f)
                    a = dict["people"]
        except:
            pass
root = tk.Tk()
root.title('Image')
root.geometry("800x600")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

c=0
for j in a:
    c+=1
    b = j["pose_keypoints_2d"]

    print(c, "人目")
    print("右肩:x座標 =", b[6], ", y座標 =", b[7], ", 信頼度 =", b[8])
    print("首:x座標 =", b[3], ", y座標 =", b[4], ", 信頼度 =", b[5])
    print("左肩:x座標 =", b[15], ", y座標 =", b[16], ", 信頼度 =", b[17])

    canvas.create_line(b[3]/2, b[4]/2, b[6]/2, b[7]/2)
    canvas.create_line(b[3]/2, b[4]/2, b[15]/2, b[16]/2)

root.mainloop()