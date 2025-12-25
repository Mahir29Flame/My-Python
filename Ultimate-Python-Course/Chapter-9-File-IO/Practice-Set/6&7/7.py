with open("Chapter-9-File-IO/Practice-Set/6&7/log.txt", "r") as file:
    lines = file.readlines()
    lineno = 1
    for line in lines:
        if "python" in line.lower():
            print("The Word 'Python' is present in line number ",lineno)
        lineno += 1
