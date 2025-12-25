with open("Chapter-9-File-IO/Practice-Set/8/this.txt", "r") as file:
    content = file.read()
with open("Chapter-9-File-IO/Practice-Set/8/copy_of-this.txt", "w") as file:
    file.write(content)    