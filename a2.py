import json
import math

with open("catalog.json", "r") as f:
    dict = json.load(f)

c=0
max=0
min=math.inf
for i in dict:
    if i["name"] == "jacket":
        c += 1
        if i["price"] > max:
            max = i["price"]
        if i["price"] < min:
            min = i["price"]
            
print('jacketの個数=',c)
print('jacketの最高価格=',max)
print('jacketの最低価格=',min)


