def PSlice(n):
    for i in range(n+1):
        print("*"*n)
        n -= 1
n = int(input("Enter a number of rows: "))
PSlice(n)        