class Book:
    def __init__(self, pageNo) -> None:
        self.pageNo = pageNo
        
    def __add__(first, second):  #magic method for + operator
        return (first.pageNo + second.pageNo)
        
b1 = Book(100)
b2 = Book(200)
print(b1+b2)