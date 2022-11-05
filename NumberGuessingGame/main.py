# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:01:47 2022

@author: Nicolas
"""
import replit
import random
# import logo

logo='''
   ___                       _   _           
  / _ \_   _  ___  ___ ___  | |_| |__   ___  
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \ 
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ 
\____/ \__,_|\___||___/___/  \__|_| |_|\___| 
                                             
                       _                     
 _ __  _   _ _ __ ___ | |__   ___ _ __       
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|      
| | | | |_| | | | | | | |_) |  __/ |         
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|         
                                       '''
                                       
print(logo.logo)
print("Welcome to the Number Guessing Game!")
print("i\'m thinking of a number between 1 and 100.")

secret_number=random.randint(1, 100)
attemps=0
end_of_game=False

def difficulty():
    level=input("Chooce a difficulty. Type 'easy' or 'hard': ").lower()
    if level=="easy":
        return attemps + 10
    elif level=="hard":
        return attemps + 5
    else:
        print("Invalid statement")
        difficulty()
    print(f"You have chosen the {level} level")
    
attemps=difficulty()

def make_a_guess():
    guess=int(input("Make a guess: "))
    if guess==secret_number:
        print(f"You got it! The answer is: {secret_number}")
        end_of_game=True
        new_game=input("Want to play again?")
        if new_game=="yes":
            clear()
        elif new_game=="no":
            clear()
            print(logo.logo)
    elif guess<secret_number:
        print("Too low.\nGuess again.")
        return attemps -1
    elif guess>secret_number:
        print("Too High.\nGuess again.")
        return attemps -1

while end_of_game==False:
    attemps=make_a_guess()
    print(f"You have {attemps} attemps left.")
    if attemps==0:
      print("You have run out of guesses, you lose")
      end_of_game=True
