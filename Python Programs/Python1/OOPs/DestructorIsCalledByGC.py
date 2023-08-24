import gc

class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Destructor called for {self.name}")

# Create an instance of MyClass
obj = MyClass("Object")

# Remove the reference to the object
# obj = None

# Manually invoke garbage collection
gc.collect()

print("End of program")
