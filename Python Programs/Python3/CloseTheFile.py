files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)
    #files[i].close()