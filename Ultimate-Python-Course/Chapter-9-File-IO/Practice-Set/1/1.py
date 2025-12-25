with open("C:/Users/Asus/Documents/GitHub/Python/Chapter-9-File-IO/Practice-Set/poem.txt") as f:
    c = f.read()
    if("Twinkle" or "twinkle" in c):
        print("The word 'Twinkle' is Present in this Content!")
    else:
        print("The word 'Twinkle' is not Present in this Content!")            
 