# This is a guess the number game.
import random #Import random package so that we can use the randint function
secretNumber = random.randint(1, 20) # Generates a random number between 1 and 20 and then assigns to the secretNumber

print('I am thinking of a number between 1 and 20.') #prints a prompt for he user

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):# Iniates a for loop until it is finally exited they have a total of 6 times
    print ('Take a guess.')
    guess = int(input())  # Prompts user to input an integrer, will break if there is a different property, maybe error handling can be built in

    if guess < secretNumber: #If the guess is lower than the secretNumber, then output
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.') #else if the guess is higher then the secretNumber, then output
    else:
        break #This condition is the correct guess!
    #For loops ends here when the correct guess is chosen. For loop also ends if the number of Guesses are more than 6.
    
#
if guess == secretNumber: # acts as a win or loss condition. If the resulting  guess variable is correct then win condition. else Lost.
    print('Good Job! You guessed my number in '+ str(guessesTaken) + ' guesses!')
else:
    print ('Nope, The number I was thinking of was ' +str(secretNumber))
    
