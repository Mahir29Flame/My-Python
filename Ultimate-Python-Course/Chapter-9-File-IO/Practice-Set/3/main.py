def multiplier(num=2,nums=20):
        for x in range (2,nums+1):
            with open(f"Chapter-9-File-IO/Practice-Set/3/Table_of-{x}.txt","w") as f:
                for i in range (1,11):
                    f.write(f"{num} X {i} = {num * i}\n")
            num = num + 1
task = multiplier()  
