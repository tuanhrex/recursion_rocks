# You will have to figure out what parameters to include
# 

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
import random
def coin_flips(n):
    
    if type(n) != int:
        raise TypeError('Value must be a positive integer')
    if n < 1:
        raise ValueError('Value must be a positive integer')
    if n == 1: 
        return ['H', 'T']

    already_flipped = coin_flips(n - 1)

    history_plus_heads = list(el + 'H' for el in already_flipped)
    history_plus_tails = list(el + 'T' for el in already_flipped)

         
    return history_plus_heads + history_plus_tails


    

print(coin_flips(4)) 
# => ["HH", "HT", "TH", "TT"]