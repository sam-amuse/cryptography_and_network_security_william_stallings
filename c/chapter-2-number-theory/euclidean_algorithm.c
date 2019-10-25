/*
 ============================================================================
 Name        : c.c
 Author      : Samir BEN DODO
 Version     :
 Copyright   : 
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int euclidean_gcd(int a, int b);

#define DEBUG 1

#ifdef DEBUG
#define _DEBUG printf
#else
#define _DEBUG(...)
#endif

int euclidean_gcd(int a, int b)
{
	_DEBUG("A = %d , B = %d \n",a,b);
	int a_tmp =a;
	int b_tmp =b;
	int temp;
	while(b != 0 )
	{
		temp=a%b;
		a=b;
		b=temp;
	}
	_DEBUG("euclidian GCD(%d,%d) = %d \n\n",a_tmp, b_tmp, a);
	return a;

}

int recursive_euclidean_gcd(int a, int b)
{
	_DEBUG("A = %d , B = %d \n",a,b);
	int a_tmp =a;
	int b_tmp =b;

	if(b == 0)
	{
		_DEBUG("recursive euclidian GCD(%d,%d) = %d \n",a_tmp,b_tmp,a);
		return a;
	}
	return recursive_euclidean_gcd(b,a%b);
}


int main(void) {
	euclidean_gcd(234,51);
	recursive_euclidean_gcd(234,51);
	return EXIT_SUCCESS;
}
