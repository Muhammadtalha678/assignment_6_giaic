class Engine:
    def start(self):
        print("Engine start") 
        

class Car:
    def __init__(self):
        self.engine = Engine()
        self.engine.start()
        print("Car start ")

c = Car()

del c


e = Engine()
print(e.start())