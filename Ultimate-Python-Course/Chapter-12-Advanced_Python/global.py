a = 6789876
def fun():
    global a
    a = 45
    print(a)
fun() # a changes to 45 when fun() is called
print(a) 