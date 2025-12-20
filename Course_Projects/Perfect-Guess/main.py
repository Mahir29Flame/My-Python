from random import randint
def guesser(score=0):
    play = True
    while play == True:
        selection = input("Which difficulty lvl u wanna choose (Easy/Medium/Hard/Exit) : ")
        def easy():
            nonlocal score
            num = randint(1,50)
            print("The Number is between 1 to 50")
            for i in range(10):
                print ("You have",(10-i),"Guesses left!")
                guess = int(input("Type your guess here (ctrl+c to exit): "))
                if guess == num :
                    print("YES!!!! You have done it!!!!\n")
                    score += 50
                    
                    break
                else:
                    score -= 2
                    if num>guess :
                        print("Hint: The number is Greater\n")    
                    elif num<guess :
                        print("Hint: The number is Smaller\n")
            else:
                print("The number was ",num)
            print("Your Score: ",score)
        def medium():
            nonlocal score
            num = randint(1,200)
            print("The Number is between 1 to 200")
            for i in range(15):
                print ("You have",(15-i),"Guesses left!")
                guess = int(input("Type your guess here (ctrl+c to exit): "))
                if guess == num :
                    print("YES!!!! You have done it!!!!\n")
                    score += 200
                    break
                else:
                    score -= 10
                    if num>guess :
                        print("Hint: The number is Greater\n")    
                    elif num<guess :
                        print("Hint: The number is Smaller\n")
            else:
                print("The number was ",num)
            print("Your Score: ",score)

        def hard():
            nonlocal score
            num = randint(1,500)
            print("The Number is between 1 to 500")
            for i in range(10):
                print ("You have",(10-i),"Guesses left!")
                guess = int(input("Type your guess here (ctrl+c to exit): "))
                if guess == num :
                    print("YES!!!! You have done it!!!!\n")
                    score += 500
                    break
                else:
                    score -= 25
                    if num>guess :
                        print("Hint: The number is Greater\n")    
                    elif num<guess :
                        print("Hint: The number is Smaller\n")
            else:
                print("The number was ",num)            
            print("Your Score: ",score)      
        if selection.lower() == "exit":
            return score
            break
        elif selection.lower() == "easy":
            easy()
        elif selection.lower() == "medium":
            medium()
        elif selection.lower() == "hard":
            hard()
        else:
            print("U chose an invalid difficulty lvl")    
final_score = guesser()

with open("Course_Projects/Perfect-Guess/hiscore.txt", "r") as f:
    content = f.read().strip()
    hiscore = int(content) 

if final_score > hiscore:
    print(f"\nNew High Score: {final_score}!")
    with open("Course_Projects/Perfect-Guess/hiscore.txt", "w") as f:
        f.write(str(final_score))
else:
    print(f"\nYour Score: {final_score}")
    print(f"High Score: {hiscore}")