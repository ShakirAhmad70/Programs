import os

# print(dir()) #No parameter means current module

'''This is doc string'''
print(__doc__) #I don't know why it is not printing doc string


print('File Name:',__file__)
print('Absolute Path:',os.path.abspath(__file__))
print('Directory Name:',os.path.dirname(os.path.abspath(__file__)))