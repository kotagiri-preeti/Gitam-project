import re
with open("SDC_PYTHON.txt") as f:
    i=0
    for line in f:
        list[i]=line
        i+=1
result = re.finditer(r"[.*$",list)
for i in result:
    print(i)