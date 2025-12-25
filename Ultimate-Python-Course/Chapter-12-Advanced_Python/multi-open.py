with (
    open("Chapter-12-Advanced_Python/file1.txt") as file1, 
    open("Chapter-12-Advanced_Python/file1.txt", "w") as file2
):
    file1.read()
    file2.write("nj")