class Student:
    school_name = "Dhaka College"

    def __init__(self,name,class_of,roll,CGPA):
        # pass
        self.name = name
        self.class_of = class_of
        self.roll = roll
        self.CGPA = CGPA

    def print_everything(self):
        print(f"Name = {self.name}\nRoll = {self.roll}\nClass = {self.class_of}\nCGPA = {self.CGPA}")

    def grade(self):
        return self.CGPA
    def schoolName(self):
        return self.school_name


st1 = Student("Saikot",12,650,4.5)

st1.print_everything()

a = st1.grade()

print(a)

print(Student.school_name)

print(st1.school_name)

print(st1.schoolName())