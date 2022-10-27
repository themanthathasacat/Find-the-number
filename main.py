from random import random

a = 100*random()
number = int(a)

while True:
    guess = int(input("Please guess a number \n:"))
    if number == guess:
      print("your guess is correct")
      break
    else:
        print("Try Again")
        if (guess < number):
            print("too low")
        elif(guess > number):
            print("too high")