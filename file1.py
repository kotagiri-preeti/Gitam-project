f=open("f:/abc.txt","a")
f.write("this is another line")
txt=open("f:/abc.txt")
for i in txt:
    print(i)
#print(txt.read())
f.close()
