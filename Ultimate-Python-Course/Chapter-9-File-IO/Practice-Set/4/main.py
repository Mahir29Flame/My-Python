bad_word = "donkey"
with open("Chapter-9-File-IO/Practice-Set/4/file.txt","r") as f:
    content = (f.read()).lower()
contentnew = (content.replace(bad_word,"######")).capitalize()  
with open("Chapter-9-File-IO/Practice-Set/4/file.txt","w") as f:
    f.write(contentnew)