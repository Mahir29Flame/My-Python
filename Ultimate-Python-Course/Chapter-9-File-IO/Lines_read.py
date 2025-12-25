f = open("Chapter-9-File-IO/stupid-msg.txt")
# lines = f.readlines()
# print(lines, type(lines))

line1 = f.readline()
print(line1,type(line1))
line1 = f.readline()     ### this shows that, the same var.s can work as 2nd line and even 3rd line too
print(line1,type(line1)) 
line2 = f.readline()
print(line2,type(line2))
f.close()