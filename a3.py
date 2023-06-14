import zipfile
import re

s=0
with zipfile.ZipFile("sample.zip", "r") as zf:
    for i in zf.namelist():
        try:
            name = re.findall(r'_(.*?)_', i)
            s+=int(name[0])
        except:
            pass


print(s)