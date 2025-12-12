Name = "Mahir"

print(len(Name)) # give the lenth 

print("The name ends with ir, is :",Name.endswith("ir")) # check if the string ends with the given string-part

print("The name starts with Mah, is :",Name.startswith("Mah")) # check if the string starts with the given string-part
print("The name starts with mah, is :",Name.startswith("mah")) # IMP, that is case sensitive !


Name_2 = "nahiyan Jarif mahir"

print(Name_2.title()) # convert the first character of each word to uppercase
print(Name_2.capitalize()) # capitalize the first character and doesnt include any other words after that
print(Name_2.upper()) # convert all the characters to uppercase
print(Name_2.lower()) # convert all the characters to lowercase

print(Name_2.find("mahir")) # find the index of the given string-part
print(Name_2.count("i")) # count the number of times the given string-part occurs in the string


Name_3 = "NJ is a very good good student"

print(Name_3.replace("good","bad")) # replace the given string-part with all the given string-part
