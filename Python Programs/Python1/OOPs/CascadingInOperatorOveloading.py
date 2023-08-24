class Book:
    def __init__(self, pages):
        self.pages = pages
        
    def __str__(self):
        return f"Book({self.pages})"
        
    def __add__(self, other):
        return Book(self.pages + other.pages)
        
    def __iadd__(self, other):
        self.pages += other.pages
        return Book(self)
    
    def __mul__(self, other):
        return Book(self.pages * other.pages)
    
    def __imul__(self, other):
        self.pages *= other.pages
        return Book(self)
        
    def __sub__(self, other):
        return Book(self.pages - other.pages)
        
    def __isub__(self, other):
        self.pages -= other.pages
        return Book(self)
    
    def __div__(self, other):
        return Book(self.pages / other.pages)
    
    def __idiv__(self, other):
        self.pages /= other.pages
        return Book(self)
        
    def __floordiv__(self, other):
        return Book(self.pages // other.pages)
        
    def __ifloordiv__(self, other):
        self.pages //= other.pages
        return Book(self)
    
    def __mod__(self, other):
        return Book(self.pages % other.pages)
    
    def __imod__(self, other):
        self.pages %= other.pages
        return Book(self)
        
    def __pow__(self, other):
        return Book(self.pages ** other.pages)
        
    def __ipow__(self, other):
        self.pages **= other.pages
        return Book(self)
    
    def __eq__(self, other):
        return Book(self.pages == other.pages)
    
    def __ne__(self, other):
        return Book(self.pages != other.pages)
    
    def __gt__(self, other):
        return Book(self.pages > other.pages)
    
    def __ge__(self, other):
        return Book(self.pages >= other.pages)
    
    

b1 = Book(100)
b2 = Book(150)
b3 = Book(200)
b4 = Book(250)
b5 = Book(300)

print(b1+b2)
print(b1+b2+b3)
print(b1*b2+b3)
print(b1 == b2)
print(b1 < b2)