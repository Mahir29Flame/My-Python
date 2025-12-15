def Ftc(F,C=0):
    C = 5/9*(F-32)
    return C
F = float(input("Enter temperature in Fahrenheit: ")) 
C = Ftc(F)

print(f"The Temperature in Celsius is: {round(C,2)}°C")