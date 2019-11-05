//============================================================================
// Name        : miller_rabin.cpp
// Author      : Samir BEN DODO
// Version     :
// Copyright   : 
// Description : Miller-Rabin algorithm in C++
//============================================================================

#include <iostream>
using namespace std;


//#define DEBUG 1
#ifdef DEBUG
#define _DEBUG(x) do { std::cout << x <<endl ; } while (0)
#else
#define _DEBUG(...)
#endif

void miller_rabin(unsigned long n, int k);
unsigned long mod_exp(unsigned long base, unsigned long exponent, unsigned long modulus);


// Modular exponentiation with the square and multiply method
// based on Applied Cryptography book by Bruce Schneier
// Used to replace the C pow() function that I initialy used but that overflows
unsigned long mod_exp(unsigned long base, unsigned long exponent, unsigned long modulus){
	unsigned long result= 1;
	base = base % modulus; //reduce to modulo if number > modulo
	while (exponent > 0)
	{
		// if exponent is odd, multiply base with result
		if(exponent & 1) result = (result*base) % modulus;
		exponent >>= 1; // exponent/2
		base = (base * base) % modulus;
	}
	return result ;
}

void miller_rabin(unsigned long n, int k){
	cout<<"\nmiller-rabin : n= "<< n << " , k =" << k ;
    if (n == 2){ // n = 2, prime
    	cout<<" n is prime";
    	return; //True : prime
    }
    if (n % 2 == 0){ // n even (and different from 2), not prime
    	cout << " n is composite";
    	return;
    }
    //STEP 1 : write n-1 in the form of n-1 = 2^s*r with r odd
    unsigned long r = n-1;
    unsigned long s = 0;
    while (s % 2  == 0){
        s += 1 ;
        r /= 2 ;
    }
    _DEBUG("\nwhile : s = "<< s << "r = "<< r);
    _DEBUG("\nn-1 \t= 2^(s) \t* r");
    _DEBUG("\n"<<n-1<< " \t= 2^("<< s << ") \t* "<< r);
     //STEP 2 : test the mathematical condition stated at the top
    for (int i=0; i<k; i++){
        // /!\ using rand (pseudo-random) and on top of that modulus of it
    	// which focus on LSBs that have less entropy is cryptographically not secure
    	unsigned long a = rand()%n ;

        _DEBUG("\nfor : a = "<< a );
        unsigned long x = mod_exp(a,r,n) ; //a^d mod n

        _DEBUG("\nx= "<< x << " =  "<< a <<"^"<< r <<" mod "<< n);
        if (x == 1  || x == (n-1)){
            _DEBUG("\nx= 1 or -1 for  "<< a <<"^"<<r <<" mod "<<n);
            continue;
        }
        int found = 0;
        for (unsigned long j=1; j<s; j++){
            x = mod_exp(a,x,n);
            _DEBUG("\nloop (0->s-1) : x^2= "<< x << " =  "<< a << "^"<< r <<"*2^"<< j <<" mod "<< n);
            if (x == n-1){
                _DEBUG("\nx= n-1 for "<< x << "^2 mod "<< n);
                found = 1; // True
                break;
            }
        }
        if (found == 0){
        	cout<<" n is composite";
        	return; //False : both test failed, not prime
        }
    }
    cout<<" n is prime" ;
    return;//True : probably prime
}

