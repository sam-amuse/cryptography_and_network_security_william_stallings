'''
Created on 23 oct. 2019
Optimal version of the Euclidean algorithm (code compact)
@author: Samir BEN DODO
'''

from math import floor

def euclid_algo(a, b, verbose):
    while b:
        a, b = b, a % b    
        if verbose and b != 0: print('%s = %s * %s + %s' % (a, floor(a/b), b, a % b))
    if verbose: print('\nGCD is %s \n' % a)
    return a

euclid_algo(283, 32874, False)
euclid_algo(8334,93274, True)
euclid_algo(3767,7919, True) 