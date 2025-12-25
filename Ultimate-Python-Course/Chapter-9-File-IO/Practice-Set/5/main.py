bad_words = ["donkey","stupid","idiot","autistic","noob","dumb","homeless","coward"]

with open("Chapter-9-File-IO/Practice-Set/5/file.txt","r") as f:
    content = f.read().lower()

for word in bad_words:
    content = content.replace(word, '#'*len(word))

content = content.title()

with open("Chapter-9-File-IO/Practice-Set/5/file.txt","w") as f:
    f.write(content)