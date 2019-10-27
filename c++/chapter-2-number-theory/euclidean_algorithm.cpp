//============================================================================
// Name        : euclidean_algorithm.cpp
// Author      : Samir BEN DODO
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#define DEBUG 1

#ifdef DEBUG
#define _DEBUG(x) do { std::cout << x ; } while (0)
#else
#define _DEBUG(...)
#endif

int euclidean_gcd(int a, int b)
{
	//_DEBUG("A = "<< a << " B = "  << b );
	int a_tmp =a;
	int b_tmp =b;
	int temp;
	while(b != 0 )
	{
		temp=a%b;
		a=b;
		b=temp;
	}
	_DEBUG("\neuclidian GCD("<< a_tmp << "," << b_tmp <<") = " << a <<"\n");
	return a;

}

int recursive_euclidean_gcd(int a, int b, int level = 0)
{
	if(level == 0){
		_DEBUG("\nrecursive euclidian GCD("<< a <<","<< b <<") = ");
	}

	if(b == 0)
	{
		_DEBUG(a);
		return a;
	}
	return recursive_euclidean_gcd(b,a%b,level+1);
}
