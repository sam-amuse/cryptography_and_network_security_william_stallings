'''
Created on 23 oct. 2019
@author: Samir BEN DODO

Miller-Rabin Algorithm 

Mathematic background of the algorithm
Let n be an odd prime, and let n-1 = 2^s*r where r is odd
Let a be any integer such that gcd(a,n) = 1.
Then either 

Positive form
a^r = 1 or -1 (mod n) 
OR 
a^(r*2^j) = -1 (mod n) for some j such as 0 =< j =< s-1

Negative form
a^r != 1 and -1 (mod n) 
AND 
a^(r*2^j) != -1 (mod n) for some j such as 0 =< j =< s-1

'''
from random import *

def miller_rabin(n, k, verbose):
    if verbose : print ('miller-rabin called with n= %s k= %s and verbose= %s' %(n, k,verbose))
    if n == 2 : # n = 2, prime
        return True
    if n % 2 == 0 :  # n even (and different from 2), not prime
        return False
    # STEP 1 : write n-1 in the form of n-1 = 2^s*r with r odd 
    r = n-1
    s = 0
    while s % 2  == 0 : 
        s += 1
        r //= 2 #floor
        if verbose : print ('while : s = %s r = %r' %(s,r))
    if verbose : print ('n-1 \t= 2^(s) \t* r')
    if verbose : print ('%s \t= 2^(%s) \t* %s' %(n-1,s,r))
     # STEP 2 : test the mathematical condition stated at the top 
    for i in range(0,k):
        a = randrange(2,n-2) 
        if verbose : print('for : a = %s' %(a) ) 
        x = pow(a,r,n) #a^d mod n
        if verbose : print ('x= %s =  %s^%s mod %s' %(x,a,r,n))
        if (x == 1 or  x == n-1):
            if verbose : print ('x= 1 or -1 for  %s^%s mod %s' %(a,r,n))
            continue
        found = False
        for j in range (1,s):
            x = pow(a,x,n) # written better than x = pow(a,r*2**(j),n)
            if verbose : print ('loop (0->s-1) : x^2= %s =  %s^%s*2^%s mod %s' %(x,a,r,j,n))
            if x == n-1 :
                if verbose : print ('x= n-1 for  %s^%s mod %s' %(x,2,n))
                found = True
                break
        if not found : 
            return False # both test failed, not prime
    return True # probably prime

def inv_miller_rabin(n, k, verbose):
    if verbose : print ('miller-rabin called with n= %s k= %s and verbose= %s' %(n, k,verbose))
    if n == 2 : # n = 2, prime
        return True
    if n % 2 == 0 :  # n even (and different from 2), not prime
        return False
    # STEP 1 : write n-1 in the form of n-1 = 2^s*r with r odd 
    r = n-1
    s = 0
    while s % 2  == 0 : 
        s += 1
        r //= 2 #floor
    # STEP 2 : test the mathematical condition stated at the top
    for i in range(0,k):
        a = randrange(2,n-2)  
        x = pow(a,r,n) #a^d mod n
        if (x != 1 and  x != n-1):
            for j in range (1,s):
                x = pow(a,x,n)
                if x != n-1 :
                    return False    
    return True # probably prime

# if n < 2,047, it is enough to test a = 2;
#k = 2
#n = 10000139
k = 10
n = 561
verbose = False
# With k =10 , a small Carmichael number such as 561 is detected as composite
# but with a smaller k (ie 2), it can be wrongly considered prime
# This illustrates the probabilistic behavior of the Miller-Rabin algorithm
print ("n = ",n,", k=",k)
prime = miller_rabin(n, k,verbose)
if prime == True :
    print ("my program : n is prime ")
elif prime == False:
    print ("my program : n is not prime (composite)")
  
inv_prime = inv_miller_rabin(n, k,verbose)
if prime == True :
    print ("my inv program : n is prime ")
elif prime == False:
    print ("my inv program : n is not prime (composite)") 
