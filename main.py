import random

from tools.config import MOHRE
from tools.config import FIRST_COIN

from tools import text
from tools import help_text

import sqlite3

from tools.db import insert_valeus
from tools.db import login_select
from tools.db import coins
from tools.db import coin_from_db


import time

def first_text():
    print(text)
    member_choice = input("Enter your choice? ").lower()
        
    if member_choice == 'h':
        help()
    elif member_choice == "l":
        login()
    elif member_choice == "s":
        sign_up()


def help():
    print(help_text)


# player choices s k q for game
def player_choice():
    user_choice = input("What your choice(s, k, q)?: ").lower()
    if user_choice not in MOHRE:
        print("Oh Your choice is not True!, Try Again...")
        return player_choice()
    
    return user_choice


# choice whait is winner in the game
def choice_winner():
    global score_bord
    global user_coin
    global username
    
    user_coin = coin_from_db(username)
    
    # add coin dont remember
    if score_bord["bot"] > score_bord[player_name]:
        user_coin -= 1
        coins(username=username, user_coin=user_coin)
        print("--------------------------")
        print("-      Bot IIS winner    -")
        print("--------------------------")
        print(score_bord, '\n')
        
    elif score_bord[player_name] > score_bord["bot"]:
        user_coin += 1
        coins(username=username, user_coin=user_coin)
        print("----------------------------")
        print(f"-    {username} IS Winner    -")
        print("----------------------------")
        print(score_bord)
        
    else:
        user_coin += 0
        coins(username=username, user_coin=user_coin)
        print("The Game Drawed!\n")
    again_game = input("You wanna Play Again`s Game?(y, n) ")
    
    return again_game


# play game in the this func
def play():

       #name player for game
    global player_name
    player_name = username

    # choice round game
    global count
    count = int(input("How many rounds? "))

    global score_bord
    score_bord = {
    'bot': 0,
    'draw': 0,
    player_name: 0,
        
    }

    for i in range(count):
        
        player = player_choice()
        BOTMOHRE = random.choice(MOHRE)
        
        if BOTMOHRE == 'k' and player == 'k':
            score_bord["draw"] += 1
            print(score_bord)
            
        elif BOTMOHRE == 's' and player == 's':
            score_bord["draw"] += 1
            print(score_bord)
   
        elif BOTMOHRE == 'q' and player == 'q':
            score_bord["draw"] += 1
            print(score_bord)
   
   
        elif BOTMOHRE == 's' and player == 'q':
            score_bord["bot"] += 1
            print(score_bord)
        
        elif BOTMOHRE == 'k' and player == 's':
            score_bord["bot"] += 1
            print(score_bord)                
        
        elif BOTMOHRE == 'q' and player == 'k':
            score_bord['bot'] += 1
            print(score_bord)        
                
                
        elif BOTMOHRE == 's' and player == 'q':
            score_bord[player_name] += 1
            print(score_bord)
        
        elif BOTMOHRE == 'q' and player == 'k':
            score_bord[player_name] += 1
            print(score_bord)
         
        elif BOTMOHRE == 'q' and player == 's':
            score_bord[player_name] += 1
            print(score_bord) 

        count +=1
    win = choice_winner()
    if win == 'y':
        play()
        choice_winner()
    
    elif win == 'n':
        print('game finish')


# sign up gor play in the game
def sign_up():
    global username
    global password
    global email
    
    username = input("enter your username: ")
    password = input("enter your password: ")
    email = input("enter your email: ")

    tup = (username, password, email, FIRST_COIN)

    try:
        insert_valeus(tup)
        print(f"Welcome {username}\n")
        print("Now can login ths game and play!\n")
        first_text()
        
    except sqlite3.OperationalError:
        print("Error")
    
    except sqlite3.IntegrityError:
        print("username already have")
        return sign_up() 
    
    
def login():
    global username
    username = input("Enter username ")
    global password
    password = input("Enter password ")
    loging = login_select(username, password)
    coin = coin_from_db(username)
    
    if loging:
        print("Loading...")
        time.sleep(3)
        print("-----------------------------------------------")
        print(f"Name : {username} coin : {coin}")
        play()
    else:
        print("you are not login")
        return login
        
        
def show_profile():
    pass
        
if __name__ == "__main__":
    first_text()
    