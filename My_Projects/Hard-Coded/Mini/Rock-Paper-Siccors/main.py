def game():
    import random
    score = 0
    print("Welcome to the Rock-Paper-Scissors Game! 🪨📃✂️!")
    while True:
        computer = random.choice([1,0,-1])
        youstr = input("Enter your choice(R/P/S) or Q to Exit: ").lower()
        
        if youstr == 'q':
            break

        youdict = {
        'r' : 1,
        'p' : -1,
        's' : 0
        }
        reversedict = {
        1 : "Rock 🪨",
        -1 : "Paper 📃",
        0 : "Scissors ✂️"
        }
        
        if youstr not in youdict:
            print("Invalid input! Please enter R, P, or S.")
            continue

        you = youdict[youstr]
        print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]} :-")
        '''
        1 = Rock 🪨
        -1 = Paper 📃
        0 = Scissors ✂️
        '''
        if computer==you:
            print("That was a draw !!")
        else:   
            # Rock(1) beats Scissors(0)
            # Scissors(0) beats Paper(-1)
            # Paper(-1) beats Rock(1)
            
            if (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
                print("You win! 🎉🎉🎊")
                score += 2  
            else:
                print("You Loose !! 😁") 
                score -= 1     

    return score

score = game()
print(f"Game Over! Your final score is: {score}")

with open("high_score.txt", "r") as high_score:
    high_score_text = high_score.read()

if high_score_text.strip():
    high_score_num = int(high_score_text)
else:
    high_score_num = 0

if score > high_score_num:
    with open("high_score.txt", "w") as high_score:
        high_score.write(str(score))
    print(f"New high score! 🏆 Old high score was {high_score_num}")
else:
    print(f"Better luck next time! The high score is {high_score_num}")