'''
Created on 23 oct. 2019
@author: Samir BEN DODO
Extended Euclidean algorithm : a*s+b*t=gcd(a,b)
Math background in https://brilliant.org/wiki/extended-euclidean-algorithm/

Initial conditions :
s0=1, t0=0, s1=0, t1=1, a=r0, b=r1

Equations :
R(i-2) = R(i-1) * Qi + Ri
Si = S(i-2) - S(i-1) * Qi
Ti = T(i-2) - T(i-1) * Qi

Stop when R(i-1) = 0 (iteration called n) so R(n-1) = 0

Result
GCD(A,B) = R(n-2) = A*S(n-2) + B*T(n-2)
'''
def eea_algorithm(a, b, verbose):
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

eea_algorithm(1914,899, True)
