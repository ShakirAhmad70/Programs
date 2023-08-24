with open("abc.txt", "r") as f:
    print(f.tell())
    f.seek(3)
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    f.seek(2321)
    print(f.tell())
    # f.seek(-12) #ValueError : negative seek position
    print(f.read())
    f.seek(0)
