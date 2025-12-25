bn_marks = float(input("Enter Your Bangla Marks: "))
eng_marks = float(input("Enter Your English Marks: "))
math_marks = float(input("Enter Your Math Marks: "))

if (bn_marks >= 33 and eng_marks >= 33 and math_marks >= 33 and (bn_marks + eng_marks + math_marks)/3 >= 40):
    print("You have Passed 🎉🎉🎉🎉🎉 your avrg marks is ", (bn_marks + eng_marks + math_marks)/3)
else:
    print("You have failed!","Your avrg marks is ", (bn_marks + eng_marks + math_marks)/3)
    print("U Nooooob !!! 🤣🤣🤣🤣🤣")
