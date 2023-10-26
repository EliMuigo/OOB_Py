class Student:
    def __init__(self,f_name,age,ID,GPA,email,l_name):
        
        self.f_name=f_name  # These are the instance arguments
        self.age=age
        self.ID=ID
        self.GPA=GPA
        self.email=f_name+ '.'+'@gmail.com'
        self.l_name=l_name



    def fullname(self):
        return '{} {}'.format(self.f_name,self.l_name)

stud_1=Student("Jane",21,283738,3.2,"Manji")
stud_2=Student("Mike",20,324233,2.8,"Mulei")

print(stud_1.fullname()) # the fullname() becomes a method hence the use of parenthesis
print(stud_2.fullname())

#print(stud_1)
#print(stud_2)

#print(stud_1.name)
#print(stud_2.name)
#print(stud_1.email)
#print(stud_2.email)

#we can use the following line of code to display full names 
#print('{} {}'.format(stud_1.f_name,stud_1.l_name))

    
