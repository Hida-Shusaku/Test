import zipfile
import re

s=0
with zipfile.ZipFile("sample.zip", "r") as zf:
    for i in zf.namelist():
        try:
            name = re.findall(r'_(.*?)_', i)
            n=int(name[0])
            if n%2!=0:
                s+=n
        except:
            pass


print(s)