class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def diplay(self):
        print(f"student Name: {self.name}, Student Marks: {self.marks}")
student = Student("Talha",80)

student.diplay()
