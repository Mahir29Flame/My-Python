class Employee:
    company = "ITC"
    name = "NJ"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder(Employee):
    language = "Python"
    def printLanguage(self):
        print("Outta Alla Langs - its ur's - ",self.language)

class Programmer(Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        
a = Employee()
b = Programmer()
b.showLanguage()