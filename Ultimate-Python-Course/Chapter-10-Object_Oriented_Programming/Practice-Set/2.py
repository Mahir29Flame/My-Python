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
            print(self.num ** options[task])
        else:
            print("Invalid operation selected")

num = int(input("Enter a number: "))
calculator = Calculator(num)
