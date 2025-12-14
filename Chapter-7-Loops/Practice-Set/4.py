n = float(input("Enter a number: "))
prime = None
for x in range(2,int(n)):
    reminder = n%x
    if reminder == 0:
        prime = False
        break
    else:
        x += 1
        continue
if prime == None:
    print("Prime")
else:
    print("Not Prime")

    
print ("DONE!")    