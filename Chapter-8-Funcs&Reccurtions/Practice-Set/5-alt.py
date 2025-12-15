def PSlice(n):
    if n==0:
        return
    else:
        print("*"*n)
        PSlice(n-1)   
n = int(input("Enter a number of rows: "))
PSlice(n)