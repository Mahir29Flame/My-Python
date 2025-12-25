def greatest(a=1,b=1,c=1):
    if a>b and a>c:
        return a 
    elif b>a and b>c:
        return b 
    elif c>a and c>b:
        return c    
    else:
        print("All are equal")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))        
x_g = greatest(a,b,c)
print("The Greatest Number is: ",x_g)