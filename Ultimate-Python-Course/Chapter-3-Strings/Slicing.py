Name = input("Enter your name : ")
Letter_1 = Name[0]
Letter_2 = Name[1]
Letter_3 = Name[2]
Letter_4 = Name[3]
Letter_5 = Name[4]
print("1st letter of your name is :",Letter_1)
print("2nd letter of your name is :",Letter_2)
print("3rd letter of your name is :",Letter_3)
print("4th letter of your name is :",Letter_4)
print("5th letter of your name is :",Letter_5)
Sliced_Name = Name[0:3] # this means - start from index 0 and end before index 3
print("Sliced name is :",Sliced_Name)
sliced_name_2 = Name[-4:] # Leave the second number EMPTY to go to the very end
print("Sliced name 2 is :",sliced_name_2)