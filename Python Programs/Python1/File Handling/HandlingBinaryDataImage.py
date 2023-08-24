#Binary data = image, video, audio etcetera

f1 = open("guido.jpg", 'rb')
data = f1.read()
print(type(data)) #bytes

f2 = open("ShakGuido.jpeg",'wb')
f2.write(data)
