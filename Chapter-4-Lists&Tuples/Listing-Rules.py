# changing a character from a string isnt possible
Name = "Mahir"
print(Name)
# Name[4] = "N" # Saw the output ? 

# but for lists, it is possible

list = ["Mahir","Bogura", "BZS29s", 29]
print("Original list: ",list)
list[1] = "Gabtoli"
print("Updated list(v2.0): ",list)

# We can add/remove or modify a list

list.append("Ahad")

print("List v3.0 is :", list)

list.insert(3,"Cows")

# We can sort lists

nl1 = [1,5678,66345,33,0.567,733,45678,6667,77,123456789]
print("\n\nThe Num. List is now :",nl1)
nl1.sort()
print("\nWhich is now :",nl1)
nl1.reverse()
print("\nIt is now (v3) :", nl1,("\n  Just by some simple line of code"))
nl1.remove(33)
print("\nRemoved 33 :\n",nl1)
#for letters 
list[4] = ("Pros")
list.sort()
print("\n",list)