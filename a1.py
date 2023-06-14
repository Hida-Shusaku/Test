with open("data.txt", "r") as f:
    s=0
    for i in f:  
        try:
            n = int(i)
            s += n
        except ValueError:
            pass

print(s)