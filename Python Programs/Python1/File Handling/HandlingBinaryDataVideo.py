#Binary data = image, video, audio etcetera

f1 = open("durga.mp4", 'rb')
data = f1.read()
print(type(data)) #bytes

f2 = open("ShakDurga.mp4",'wb')
f2.write(data)
