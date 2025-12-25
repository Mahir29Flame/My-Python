def table(num):
    for i in range(1,11):
        print(f"{num} X {i} = ",num*i)
    return num*i
        

        
        
num = int(input("Which number's table do u want ? : "))        
table(num)