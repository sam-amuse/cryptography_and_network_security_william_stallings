'''
Created on 5 nov. 2019
@author: Samir BEN DODO

Chinese Remainder Theorem (using EEA)


'''
#from extended_euclidean_algorithm import  eea_algorithm

# brute force modular inverse function
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def eea_for_crt(a, b, verbose = False): # modified version of eea_algorithm
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    
    while r != 0 :
        # // operator does integer division (quotient without remainder)
        quotient = old_r//r 
        old_r, r = r, old_r - quotient * r 
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if verbose and b != 0: print('GCD(%s,%s) =  %s = %s*%s + %s*%s' % (a,b,old_r,a,old_s,b,old_t))  
    ''' 
    To find multiplicative inverse of 'a' modulus 'm'
    EEA is used  : ax + by = gcd(a, b) (EEA)
    with b = m , 
    ax + my = 1 (mod m)
    ax = 1 (mod m) 
    x -> multiplicative inverse of 'a' mod 'm'
    '''
    return old_s # it is x , if modular inverse exist ?


def crt(num, rem,k ,verbose = False):
    # Compute product of all numbers 
    prod = 1
    for i in range(0, k) : 
        prod = prod * num[i] 
  
    # Initialize result 
    result = 0
  
    # Apply above formula 
    for i in range(0,k): 
        pp = prod // num[i] 
        result = result + rem[i] * eea_for_crt(pp, num[i]) * pp       
    return result % prod 
  
num = [3, 4, 5] 
rem = [2, 3, 1] 
k = len(num) 
print( "x is " , crt(num, rem, k))   

                 
    