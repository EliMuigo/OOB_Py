# Class Variables- variables that are shared among all instances of a class.

class Employee:

    raise_amount=1.04

    def __init__(self,f_name,l_name,pay,email):
        self.f_name=f_name
        self.l_name=l_name
        self.pay=pay
        self.email=f_name+ '.'+l_name+"@gmail.com"
        


    def fullname(self):
        return'{} {}'.format(self.f_name,self.l_name)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    







emp_1=Employee("Jane","Wendi",5000,"JaneWendi@gmail.com")
emp_2=Employee("Corey","Schafer",6000,"CoreySchafer@gmail.com")

print(emp_1.__dict__)#printing out the dictionary

#print(emp_1.fullname())
#print(emp_2.fullname())



#print(emp_1.pay)
#print(emp_1.raise_amount)


        