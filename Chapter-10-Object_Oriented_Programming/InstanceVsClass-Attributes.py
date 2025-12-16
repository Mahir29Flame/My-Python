class Employee:
    lang = "Bhoo"
    task = "Stupidity"
    salary = -1000
cow = Employee()   # cow is the object here !
cow.name = "Motu" # Instance Attribute
cow.lang = "moo" # Instance Attribute
print("Name:",cow.name)
print("Language:",cow.lang)    # Instance Attributes are chosen over Class Attributes
print("Task:",cow.task)
print("Salary:",cow.salary)    