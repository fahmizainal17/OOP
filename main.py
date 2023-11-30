#Python Object-Oriented Programming

class Employee:
    def __init__(self,first,last,pay):   #use init method , but when we do all ,we pass first here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yakku.com'
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
        

emp_1 = Employee('Fahmi','Zainal','5000')
emp_2 = Employee('Safwan','Ali','5000')

print(emp_1)
print (emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(emp_1.fullname())
