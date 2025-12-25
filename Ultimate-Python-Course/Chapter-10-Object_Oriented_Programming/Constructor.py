class Employee:
    language = "JS" # This is a class attribute
    salary = 1200000
    def __init__(self, name, language, salary):     # this is a dunder method, which is auto-called!
        print("Im creating an object")
        self.salary = salary
        self.language = language
        self.name = name

    def getInfo(self):
        print(f"The name is {self.name}. The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")    

harry = Employee("NJ","Python",120000000)
# harry.language = "JavaScript" # This is an instance attribute
# harry.greet()
harry.getInfo()