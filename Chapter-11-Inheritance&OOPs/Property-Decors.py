class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    @property
    def name (self):
        return "The first name is " + self.fname + " and the last name is " + self.lname
    @name.setter    
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45
e.b = 56

e.name = "NJ Mahir"
print(e.name)