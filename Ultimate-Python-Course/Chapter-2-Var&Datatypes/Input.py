no_1 = input("Enter a number: ")
no_2 = input("Enter a number: ")
print("no 1 is",no_1)
print("no 2 is",no_2)
print(no_1,"+",no_2,"=", no_1 + no_2)
print ("oooooooooooo!!!! why u know that ??") # ans: input is taken as strings- not float or int!

# but we can fix this by converting them
no_1 = int(no_1)
no_2 = int(no_2)
print("But it's now :")
print(no_1,"+",no_2,"=",no_1 + no_2)

print("Just Niceee")
