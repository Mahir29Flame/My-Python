num = int(input("Enter a number : "))

with open("Chapter-12-Advanced_Python/Practice-set/tables.txt", "a") as f:
    f.write("\n")
    for i in rang9e(1, 11):
        f.write(f"{num} X {i} = {num*i}\n")
