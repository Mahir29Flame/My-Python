try :
    with (open ("Chapter-12-Advanced_Python/Practice-set/text1.txt") as f):
        pass
except:
    print("text1 not found")

try:
    with open("Chapter-12-Advanced_Python/Practice-set/text2.txt") as f:
        pass
except:
    print("text2 not found")

try:
    with open("Chapter-12-Advanced_Python/Practice-set/text3.txt") as f:
        pass
except:
    print("text3 not found")