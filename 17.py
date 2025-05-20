# 17. Class Decorators

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    # Class me method inject karna
    cls.greet = greet
    return cls

@add_greeting   
class Person:
    def __init__(self, name):
        self.name = name

# Object banakar greet call karo
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!
# print(Person.greet())  # Output: Hello from Decorator!