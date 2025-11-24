from random import randint

def rdmguessgame() :
    n=randint(1,50)
    print("I have randomly generated a number between 1 and 50, try to guess it! ")
    count=0
    guess= int(input("Enter your guess: "))
    while (guess!=n):
        if (guess>n):
            print("Too high. Guess lower!")
        elif (guess<n):
            print("Too low. Guess higher!")
        else:
            print("Invalid number.")
        count+=1
        guess= int(input("Enter your guess: "))
    print("Correct! The number was",guess,"It took you",count,"guesses!")
    
rdmguessgame()