class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self,department):
        self.department = department
        print(f"employee works at the {self.department.name} department")

d = Department("Science")

e= Employee(d)

del e

print(d.name)