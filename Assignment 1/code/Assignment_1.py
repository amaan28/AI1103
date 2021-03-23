#EP20BTECH11015 Assignment - 1
                ##QUESTION##
# A bag contains 2 white and 1 red balls.
# One ball is drawn at random and then 
# put back in the boxafter noting it’s color.  The process is repeated again.
# If X denotes the number of red balls recorded in thetwo draws, describe X:

                ##SOLUTION##

from random import randint
# Let 1 and 2 denote WHITE balls and 3 denote RED ball is drawn

sample_size = 10000000      #This experiment is repeated 10^7 times
event = [0, 0, 0]           #stores the outcome of each draw from the bag
simprob = [0.1, 0.1, 0.1]   #Stores the PROBABILITIES of all possible outcomes of the experiment
theoretical_probabilities = [4/9, 4/9, 1/9]     #Pre - calculated in the .TEX file

for i in range(sample_size):
    count = 0                       #Counts the no.of RED balls drawn throughout the experiment
    for j in range(1,2):
        draw = randint(1,3)         #draw denotes the outcome of each draw from the bag  
        if draw == 3:
            count+=1
    
    if count == 0:
        event[0]+=1
    elif count == 1:
        event[1]+=1
    else:
        event[2]+=1

for i in range(2):
    simprob[i] = event[i] / (sample_size)

print("Probability Distribution table of X")
print("                         X         0        1       2")
print(f"Values from simulation: P(X) {simprob}")
print(f"Theoretical values:     P(X) {theoretical_probabilities}")