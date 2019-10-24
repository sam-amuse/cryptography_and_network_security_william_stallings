'''
Created on 23 oct. 2019
Euclidean algorithm  is procedure to determine the greatest common divisor or two positive integers
@author: Samir BEN DODO
'''
from math import floor

import logging
import sys
log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.DEBUG)
log.addHandler(out_hdlr)
log.setLevel(logging.DEBUG)
#log.setLevel(logging.INFO)


print("Enter A and B to find GCD(A,B)")

a = int( input("A = "))
b = int( input("B = "))

if a<b :
    a,b = b,a #swap a and b

a_temp =a
b_temp =b

remainder =1
# R : remainder, Q : quotient
# equation : R(n-2) = Q(n)*R(n-1) + R(n)   
while remainder != 0 :
    quotient = floor(a_temp/b_temp)
    remainder = a_temp%b_temp
    a_temp=b_temp
    b_temp= remainder
    
    log.debug("new A = %d", a_temp)
    log.debug("new B = %d", b_temp)
    log.debug("A/B = %d", quotient)
    log.debug("Amod(B) %d= ", remainder)
    
print ("GCD(",a,",",b,") =", a_temp)
