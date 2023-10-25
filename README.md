## <b>Class</b> 
This is a blueprint of creating an instance of a class.

~~~
class Student:
    def __init__(self,name,age,ID,GPA):
        self.name=name
        self.age=age
        self.ID=ID
        self.GPA=GPA

stud_1=Student("Jane",21,283738,3.2)
stud_2=Student("Mike",20,324233,2.8)

#print(stud_1)
#print(stud_2)

print(stud_1.name)
print(stud_2.name)

~~~