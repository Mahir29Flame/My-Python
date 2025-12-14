s1 = {"Cow","NJ",2,4,23456,982,44,229,9,4567,121,543,2,2,2} 
print(s1)
s1.add("Cat") # we can add things
print(s1)
s1.remove("Cat") # we can remove things
print(s1)
# but we can't modify the items
s1.update("Cat","Rat") # so how it messed up ! 🤣
print(s1)
# nor we can do this
# s1[5] = "Stupid"
# Nothing is weirder than this, it is more than the .update() method
# s1.pop("NJ") # Saw that ? - we cant give arguments to pop()
s1.pop() # who would want this stupid command ? - IDK!
print(s1) # it will remove the first element, and the sorting of it is random !!! - is there any meaning of that !

# This Clears ur set
s1.clear()
print(s1)

