import random
computer = random.choice([1,0,-1])
youstr = input("Enter your choice(S/W/G): ").lower()
youdict = {
   's' : 1,
   'w' : -1,
   'g' : 0
}
reversedict = {
   1 : "Snake",
   -1 : "Water",
   0 : "Gun"
}
you = youdict[youstr]
print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]} :-")
'''
1 = snake
-1 = water
0 = gun
'''
if computer==you:
   print("That was a draw !!")
else:   
   if you == 1 and computer == -1:
      print("You win! 🎉🎉🎊")   
   elif you == -1 and computer == 1:
      print("You Loose !! 😁")   
   elif you == 1 and computer == 0:
      print("You Loose !! 😁")   
   elif you == 0 and computer == 1:
      print("Your win !!!!!!!! 🎉🎉🎊")  
   elif you == 0 and computer == -1:
      print("You Loose !! 😁")   
   elif you == -1 and computer == 0:
      print("Your win !!!!!!!! 🎉🎉🎊")
   elif you == 0 and computer == -1:
      print("You Loose !! 😁")       
   else:
      print("Something went wrong ! 🛑") 
