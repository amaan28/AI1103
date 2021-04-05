                                    ##PROBLEM##
# Two players A, and B alternately keep rolling a fair dice.
# The person to get a six first wins the game. 
# Given that player A starts the game, the probability that A wins the game is:
# A: 5/11 
# B:1/2
# C:7/13 
# D:6/11

                                    ##SOLUTION##

from random import randint as ri
no_of_games = 1771561
no_of_throws = 1771561
A = 0                       #A = No.of wins for Player A
B = 0                       #B = No.of wins for Player B

#Game
#Rule: First one to get 6 WINS THAT game
for j in range(no_of_games):
    for i in range(no_of_throws):
        dice = ri(1, 6)             #Outcome of each throw
        if (dice == 6):
            if (i % 2) == 0: 
                A += 1
                break
            else:
                B += 1
                break

th = 6/11                     #Theoretical value
sim = (float)(A/no_of_games)    #Values from simulation
print(f"Theretical values: {th}")
print(f"Values from simulation: {sim}")
