/*
 ============================================================================
 Name        : euclidean_algorithm.c
 Author      : Samir BEN DODO
 Version     :
 Copyright   : 
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

void eea_algorithm(int a, int b);

#define DEBUG 1

#ifdef DEBUG
#define _DEBUG printf
#else
#define _DEBUG(...)
#endif

void eea_algorithm(int a, int b){
	int s = 0, old_s = 1, t = 1, old_t = 0 ;
    int r = b;
    int old_r = a ;
    int quotient, temp;
    while (r != 0){
	    quotient = old_r/r ;
	    temp = r;
	    r = old_r - quotient * r ;
	    old_r = temp;
	    temp = s;
	    s = old_s - quotient * s ;
	    old_s = temp;
	    temp = t;
	    t = old_t - quotient * t ;
	    old_t = temp;

    }
    _DEBUG("\nGCD(%d,%d) =  %d = %d*%d + %d*%d\n", a,b,old_r,a,old_s,b,old_t);
}
