class Something:
    a = 5

o = Something()    
o.a = 0    # the variable changes but the class atttribute is still that. but it was replaced by this instance attribute 
print(o.a)
print(Something.a) # this prive that ^^ statement
