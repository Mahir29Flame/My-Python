def ItC(I=0):
    C = I * 2.54
    return C
I = int(input("Enter the value in Inches: "))    
print(f"The value-{I} in Centimeters is: {round(ItC(I),2)}") 
