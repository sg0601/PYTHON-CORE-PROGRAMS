class Employee:
    company="Google"
    salary=100
emp1=Employee()
emp2=Employee()
emp1.salary=10000
emp2.salary=20000

# CLASS ATTRIBUTE
print(emp1.company)
print(emp2.company)
Employee.company="Microsoft"
print(emp1.company)
print(emp2.company)
#OBJECT ATTRIBUTE
print(emp1.salary)
print(emp2.salary)