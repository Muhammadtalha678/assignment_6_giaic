class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Dog name is {self.name} and breed is {self.breed}")

d = Dog("Buddy", "Golden Retriever")
d.bark()