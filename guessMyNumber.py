import sys
print "Please think of a number between 0(inclusive) and 100(not inclusive)"
high = 100
low = 0
guess = (high+low)//2
while True:
    #print "Is your secret number "+str(guess)+"?"
    sys.stdout.write("Is your secret number "+str(guess)+"?")
    sys.stdout.flush()
    user_input = raw_input("Enter 'h' to indicate the guess is too high. "
    "Enter 'l' to indicate the guess is too low."
    " Enter 'c' to indicate I guessed correctly. ")
    if user_input == 'c':
        print "Game over. Your secret number was: "+str(guess)
        break
    elif user_input == 'h':
        high = guess
        guess = (high+low)//2
    elif user_input == 'l':
        low = guess
        guess = (high+low)//2
    else:
        print "Sorry, I did not understand your input." 
