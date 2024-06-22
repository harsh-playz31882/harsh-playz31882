class Employee:
    company ='ITC'
    name = 'default name'
    def show(self):
        print(f'name of employee is {self.name} and name of company is {self.company}')

    
class coder:
    language='python'
    def printLanguages(self):
        print(f'here is your language: {self.language}')


class programmer(Employee, coder):
    company='ITC infotech'
    def showLanguage(self):
        print(f'company of employee is {self.company} and language is {self.language}')


a = Employee()
b =programmer()
b.show()
b.printLanguages()
b.showLanguage()