class Car:
     def __init__(self,brand):
        self.brand = brand

     def start(self):
        print(f"{self.brand} car has started")
        
car = Car("Corola")
car.start()