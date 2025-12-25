class Animals:
    def __init__(self, name,iq=25):
        self.name = name
        self.iq = iq
    def show(self):
        print(f"The animal is {self.name} and it makes {self.sound} and has an IQ of {self.iq}")

class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("BHOW! BHOW!!!!")    

dog= Dog("laal")
dog.bark()