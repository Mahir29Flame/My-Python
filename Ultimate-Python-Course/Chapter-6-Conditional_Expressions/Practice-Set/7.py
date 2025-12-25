Ex = range(90, 101)
A = range(80, 90)
B = range(70, 80)
C = range(60, 70)
D = range(50, 60)
F = range(0, 50)
 
mark = int(input("Enter your marks: "))
if mark in Ex:
    print("Grade: Ex")
elif mark in A:
    print("Grade: A")
elif mark in B:
    print("Grade: B")
elif mark in C:
    print("Grade: C")
elif mark in D:
    print("Grade: D")
elif mark in F:
    print("Grade: F")   
    print("Greatest result in history 😁 !!") 
else:
    print("Invalid marks")
