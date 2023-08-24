from abc import abstractmethod, ABC

class Vehicle(ABC):  #To be an abstract class it must extend ABC(Abstract Base Class)
    @abstractmethod
    def noOfGears(self):
        pass
    
class Bus(Vehicle):
    def noOfGears(self):
        print("Bus has 6 gears")
    
class Bike(Vehicle):
    def noOfGears(self):
        print("Bike has 4 gears usually")
        
class SuperBike(Vehicle):
    def noOfGears(self):
        print("SuperBike has 5 gears")

bus = Bus()
bus.noOfGears()

bike  = Bike()
bike.noOfGears()

superBike = SuperBike()
superBike.noOfGears()