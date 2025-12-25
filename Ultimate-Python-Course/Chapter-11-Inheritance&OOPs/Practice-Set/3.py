class Employee:
    name = input("What's your name ? : ")
    company = "NJ29ers"
    salary = 100000
    sector = "Robotics"
    increament = 25
    print(f"The Employee's name is {name}, He works for {company}, He is paid {salary} a month, which increament {increament}% per year! He works in the {sector} sector.")
    @property
    def salaryafterincreament(self):
        return "The salary after his next increament will be",self.salary+self.salary*(self.increament/100),"$"

    @salaryafterincreament.setter
    def salaryafterincreament(self,salary):

        self.increament = ((salary/self.salary)-1)*100

some = Employee()
print(some.salaryafterincreament)
salary = 39483746
print(some.increament)