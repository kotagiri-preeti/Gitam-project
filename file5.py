file = open("ab.jpg", "wb")
with open("ab.png", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        file.write(byte[0])
