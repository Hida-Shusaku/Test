import zipfile
import re
import json

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

c=0
for j in a:
    c+=1
    b = j["pose_keypoints_2d"]

    print(c, "人目：")
    print("鼻:x座標 =", b[0], ", y座標 =", b[1], ", 信頼度 =", b[2])
    print("首:x座標 =", b[3], ", y座標 =", b[4], ", 信頼度 =", b[5])