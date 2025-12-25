with open("Chapter-9-File-IO/Practice-Set/11/file.txt", "r") as file:
    content = file.read()
with open("Chapter-9-File-IO/Practice-Set/11/renamed_by_python.txt", "w") as file:
    file.write(content)    
print("File renamed successfully")