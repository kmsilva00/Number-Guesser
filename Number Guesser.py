# Project 002 number guesser game

import random

tn = random.randint(0,100)                              # creates a target number to be guessed for the game
#print(tn)
guess = int()                                              # emepty list to hold the scores, can be used to get all time highscore ( will try to save names and value in touples
username = str()
score = int()


def start_game():
    guess = int()
    global score
    global username
    username = str(input("username:"))
    while guess != tn:
        guess: int = int(input("guess a number: "))
        if guess < tn:
            print("go higher")
            score = score + 1
        elif guess > tn:
            print("go lower")
            score = score + 1
        else:
            print("You guessed it right, your missed %s" %score + " times")

start_game()

with open('scoreboard', 'a+') as f:
    if isinstance(username, str) and isinstance(score, int):
        print('username : %s | score : %d' % (username, score))
        f.write('username : %s | score : %d \n' % (username, score))

# Improvements for the code
"""
import json

username = "ted"
score = 22

existing_scores = None
with open("scoreboard") as inf:
    existing_scores = json.load(inf)

if username not in existing_scores:
    existing_scores[username] = 0

existing_scores[username] += score

with open("scoreboard", "w") as outf:
    json.dump(existing_scores, outf)
    
"""