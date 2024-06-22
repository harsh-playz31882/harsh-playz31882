class Employee:
    a = 1

class programmer(Employee):
    b = 2 

class manager(programmer):
    c = 3


o  = Employee()
print(o.a)

o  = manager()
print(o.a, o.b, o.c)
