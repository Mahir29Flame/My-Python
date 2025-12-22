def CtF(C=0):
    F = C*9/5+32
    return F
C = float(input("Enter temperature in Celcius: ")) 
F = CtF(C)
print(f"The Temperature in Fahrenheit is: {round(F,2)}°F")
