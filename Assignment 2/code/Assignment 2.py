#EP20BTECH11015 - Assignment 2
                                    ##QUESTION##
# An unbalanced  dice  (with  6  faces,  numberedfrom  1  to  6)  is  thrown.
# The  probability  that the face value is odd is 90% of the probability that theface  value  is  even.
# The  probability  of  getting  anyeven  numbered  face  is  the  same.
# If  the  probability that the face is even given that it is greater than 3 is 0.75,
#  which one of the following options is closestto the probability that the face value exceeds 3?
# A: 0.453
# B: 0.468
# C: 0.485
# D: 0.492

                                    ##SOLUTION##
from random import randrange as rdrn

sample_size=1000000           #No.of times this experiment is performed
sample_space = [1] * 30 + [2] * 30 + [3] * 31 + [4] * 30 + [5] * 20 + [6] * 30      #Properties of the BIASED dice
rec = [0, 0, 0, 0, 0, 0]  #Records no.of times each number occured throughout the experiment

for i in range(sample_size):
    face_value = sample_space[rdrn(len(sample_space))]       #Stores the face value appeared on each throw of the dice
    rec[face_value - 1] += 1

sim_prob = float(rec[3] + rec[4] + rec[5])/float(sample_size)    #Stores the required probability of face value being more than 3
theory_prob = 0.468
print(f"Calculated values: {theory_prob}")
print(f"Values from Simulation: {sim_prob}")