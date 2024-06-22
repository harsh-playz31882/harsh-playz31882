class Employee:
    company='ITC'
    def show(self):
        print(f'name is {self.name} and salary is {self.salary}')


'''class programmer:
    company='ITC infotech'
    def show(self):
        print(f'name is {self.name} and salary is {self.salary}')


    def showLanguage(self):
        print(f'name is {self.name} and language is {self.language}')'''

class programmer(Employee):
    company='ITC Infotech'
    def showLanguage(self):
        print(f'name is {self.name} and language is {self.language}')


a = Employee()
b = programmer()

print(a.company)
print(b.company)
