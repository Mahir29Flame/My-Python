file = open("Chapter-9-File-IO/stupid-msg.txt")
pritable = int(input("How many lines do u need us to print : ")) 
for l in range(pritable):       # This is better for printing specific amount of lines
    l = file.readline()
    print(l)

#this might be a better option :
line = file.readline()
while line != "":    # this is better for printing the whole
    print(line) 
    line = file.readline()
file.close()    