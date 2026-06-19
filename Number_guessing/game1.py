import random
def func():
 secret_number = random.randint(1, 100)
 attempts = 0
 guess = None
 print("🎯 Welcome to the Number Guessing Game!")
 print("I'm thinking of a number between 1 and 100. Can you guess it?")

 while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts!")
        break
    if attempts >= 5:
        print("you lose !! better luck next time\n")  
        break
while True : 
    func()
    a=input("Do you want to play again , press 0 for yes and 1 for no\n")
    if a== '1':
      print("Thank you for playing.....Come back again!!")
      break
    elif a == '0' :
      continue
    else : 
      print("Invalid option...")
      break
   
    

    
     
