with open("Chapter-9-File-IO/Practice-Set/9/file1.txt", "r") as file1:
    content1 = file1.read()
with open("Chapter-9-File-IO/Practice-Set/9/file2.txt", "r") as file2:
    content2 = file2.read()
with open("Chapter-9-File-IO/Practice-Set/9/file3.txt", "r") as file3:
    content3 = file3.read()

if content1 == content2 == content3:
    print("All the files are identical.")
elif content1 == content2:
    print("File 1 and File 2 are identical.")
elif content1 == content3:
    print("File 1 and File 3 are identical.")
elif content2 == content3:
    print("File 2 and File 3 are identical.")
else:
    print("No files are identical.")