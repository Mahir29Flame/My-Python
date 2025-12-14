username = input("Enter Your Username: ")
if (len(username) > 10):
    print("The UserName is longer than 10 characters")
elif (len(username) == 0):   
    print("The UserName is empty, R U dumb?") 
else:
    print("The UserName is shorter than 10 characters")
    