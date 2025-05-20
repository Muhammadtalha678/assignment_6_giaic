# 20. Creating a Custom Exception

class InvalidAgeError(Exception):
    def __init__(self,age):
        super().__init__(f"Age {age} must be greater than 18")
        self.age = age

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print("Yes! You are adult")

for i in range(20):
    check_age(i)