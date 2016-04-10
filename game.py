# greeting for user
name = raw_input("Welcome to the number guessing game. What is your name? ")

# creating game
import random # random is a module
ran_num = random.randint(1,100) #chose a random number; 1 and 100 are inclusive in the range

# print ran_num # test to print the random number

# creating the function for guessing game
def guessing_game():
    print "Hi, %s. I'm thinking of a number between 1 and 100. Try to guess the number." % name
    count = 0 # initial condition
    while True: 
        try: # verifying tha input values are integers
            guess = int(raw_input("What's your guess? ")) # asks user to enter a new number
            count +=1 # for every guess the counter increments by 1
            if guess < 1 or guess > 100: 
                print "You exceeded the range. Try again."
            elif guess < ran_num:
                print "That's too low. Try again."
            elif guess > ran_num:
                print "That's too high. Try again."
            else:
                print "Congratulations! You guessed the correct number in %i tries." % count # tells the user how many guesses s/he made to get the right number
                option = raw_input('Would you like to continue playing the game? Enter "Yes" or "No" ')
                # asks the user if they want to play again. 
                if option.upper() == "YES": #typecasted the answer to upper cases to avoid capitalization errors
                    guessing_game()
                else: 
                    print "Bye bye!" # The user wants to leave the game. 
                    break
        except ValueError: # verification of input; prints the comment below if the user's input is not an integer
            print "Oops! That's not an integer. Try again"

guessing_game()


