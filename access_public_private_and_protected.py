class Employee:
    def __init__(self,name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    
employee = Employee("Talha",50000,"123-45-6789")
print(employee.name)
print(employee._salary)
try:
    print("Private: ", employee.__ssn)      
except AttributeError as e:
    print("Private: Cannot access directly -", e)
    # name mangling
print(employee._Employee__ssn)
