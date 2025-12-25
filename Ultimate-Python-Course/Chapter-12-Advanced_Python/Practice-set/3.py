List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in List:
    numtable = (num.__str__()+"table")
    numtable = [num*i for i in range(1, 11)]
    print(f"Table of {num} is : ",numtable)