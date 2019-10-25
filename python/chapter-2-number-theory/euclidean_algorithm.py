'''
Created on 23 oct. 2019
Euclidean algorithm  is procedure to determine the greatest common divisor or two positive integers
@author: Samir BEN DODO
'''
print("Enter A and B to find GCD(A,B)")

a = int( input("A = "))
b = int( input("B = "))

a_temp =a
b_temp =b
remainder =1
# R : remainder, Q : quotient
# equation : R(n-2) = Q(n)*R(n-1) + R(n)   
while remainder != 0 :
    remainder = a_temp%b_temp
    a_temp=b_temp
    b_temp= remainder
   
print ("GCD(",a,",",b,") =", a_temp)
