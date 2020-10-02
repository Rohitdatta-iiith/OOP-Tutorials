class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@iiit.ac.in'
    def fullname(self):
        return f"{self.fname} {self.lname}"
javahar = Employee('javahar','cv',200000)
pkreddy = Employee('krishna','reddy',150000)
print(javahar.email)
print(pkreddy.email)
print(Employee.fullname(pkreddy))
print(javahar.fullname())
