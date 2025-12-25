def table(num, i=1):
    if i > 10:
        return
    print(f"{num} X {i} = {num*i}")
    table(num, i + 1)

num = int(input("Which number's table do u want ? : "))        
table(num)