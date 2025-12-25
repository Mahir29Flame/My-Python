# f = open("Chapter-9-File-IO/stupid-msg.txt","a")
# data = f.read()
# print(data)
# f.close()

# The same thing can be done with 'with' statement:
with open("Chapter-9-File-IO/stupid-msg.txt") as f:
    print(f.read())
# you dont have to explicitly close the file    