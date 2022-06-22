import random
computerNumber = random.randint(0,10)
userGuess = int(input("Guess what number I am thinking of from 0 to 10: "))
if(userGuess == computerNumber): 
  print("You guessed Correctly")
else: 
  print("Wrong! My computer number was " + str(computerNumber))