import random
import art_HoL
from game_data_HoL import data

def participant():
    '''get data of a random participant in dictionary "data"'''
    return random.choice(data)

def format(participant):
    '''Format participant info into printable form'''
    name=participant['name']
    description=participant['description']
    country=participant['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    '''checks participant against user's guess'''
    print(guess, a_followers, b_followers)
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(art_HoL.logo)
    points = 0
    game_should_continue = True
    participant_a = participant()
    participant_b = participant()
    
    while game_should_continue:
        participant_a = participant_b
        participant_b = participant()
        
        while participant_a == participant_b:
            participant_b = participant()
            
        print(f"Compare A: {format(participant_a)}")
        print(art_HoL.vs)
        print(f"Compare B: {format(participant_b)}")
        
        guess1=input("Who has more followers? Type 'A' or 'B': ").lower()
        guess=guess1
        a_followers=participant_a["follower_count"]
        b_followers=participant_b["follower_count"]
        is_correct=check_answer(guess, a_followers, b_followers)
        print(art_HoL.logo)
        
        if is_correct:
            points +=1
            print(f"You\'re right! Current score: {points}")
        else:
            game_should_continue = False
            print("Sorry, that\'s wrong. Game over")
game()







     