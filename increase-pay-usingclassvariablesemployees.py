class Employee:
    num_of_emps = 0 #class atrributes
    pay_rise = 1.05
    def __init__(self,fname,lname,pay):
        self.fname = fname         #instance attributes
        self.lname = lname
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@iiit.ac.in'
        Employee.num_of_emps += 1
    def increase_pay(self):
        self.pay = int(float(self.pay) * self.pay_rise)
        
javahar = Employee('Javahar','CV',200000)
pkreddy = Employee('Krishna','Reddy','150000')
javahar.increase_pay()
#pkreddy.increase_pay()

print(javahar.pay)
Employee.pay_rise = 1.06
print(javahar.pay)
javahar.increase_pay()
print(javahar.pay)
pkreddy.pay_rise = 1.07
print(pkreddy.pay)
pkreddy.increase_pay()
print(pkreddy.pay)
