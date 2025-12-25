with open("Chapter-9-File-IO/Practice-Set/6&7/log.txt", "r") as file:
    content = file.read() 
    if "python" in content:
        print("'Python' is present in the log file")    
    elif "py" in content:
        print("'Py' is present in the log file, means it is about python but doesnt say 'Python'")    
    else:
        print("'Python' is not present in the log file")