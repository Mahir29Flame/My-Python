class Calculator:
        
    def  __init__ (self,num):
        self.num = num
        task = (input("What do u wanna do (Sqr,Sqrt,Cube: )").lower())
        options = {
            "sqr": 2,
            "cube": 3,
            "sqrt": 0.5
        }
        
        if task in options:
            print(round(self.num ** options[task],2))
        else:
            print("Invalid operation selected")

    @staticmethod
    def introduction ():
        print("Hello, I am a calculator")    # introduction added
num = int(input("Enter a number: "))
intro = Calculator.introduction()
calculator = Calculator(num)

