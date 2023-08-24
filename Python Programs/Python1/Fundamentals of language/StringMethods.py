s = 'aabcdefghijklllmnmnma'

print(s.find('g'))
print(s.find('def'))
print(s.find('deg')) #return -1 if substring not present
print(s.find('cde',2,8))
print(s.rfind('f'))
print(s.rfind('fgh'))
print(s.rfind('hgf'))

print(s.index('ghi'))
print(s.rindex('efg'))
# print(s.index('z')) #produce ValueError if substring not present
try:
    print(s.index('z'))
except ValueError:
    print("Index not found...")
    
print(s.count('a'))
print(s.count('ab'))
print(s.count('ab',3,9))
print(s.count('z'))

str = 'aaaaa'
print(str.count('aaaaa'))
print(str.count('aaaa'))
print(str.count('aaa'))
print(str.count('aa'))
print(str.count('a'))


string = '03-06-2023'
seperator = '-'
l = string.split(seperator) #will return a list
print(l)

print(seperator.join(l))

a = 'Learning pyThon Is veRy Easy. It is powerFul Too'
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())
print(a.capitalize())

print(a.startswith("Learning"))
print(a.startswith("Python"))
print(a.endswith("Too"))
print(a.endswith("Also"))

b = "asjbdfasd1231jbasd"

print(b.isalnum())
print(b.isspace())
print(b.islower())
print(b.isupper())
print(b.istitle())
print(b.isalpha())
print(b.isdigit())

sm = 'ShakirMalik'
r = reversed(sm) #reversed is not a function for string only it can reverse list also and so on
print(type(r))
ms = ''.join(r)
print(ms)