def greet(name, greeting="You are a Kid"):
    print(greeting, ",", name,"!")
    return "Thanks!"

dflt = greet(input("Enter your name: "))
print(dflt)
noob = greet(input("Enter your name: "), "You are a noob")
print(noob)
