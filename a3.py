import zipfile
import re

sum=0
with zipfile.ZipFile("sample.zip", "r") as zf:
    for i in zf.namelist():
        try:
            name = re.findall(r'_(.*?)_', i)
            n=int(name[0])
            if n%2!=0:
                with zf.open(i) as f:
                    c = f.read()
                    number = int(c)
                    sum += number
        except:
            pass

print("合計＝", sum)