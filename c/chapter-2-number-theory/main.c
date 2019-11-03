/*
 * main.c
 *
 *  Created on: 27 oct. 2019
 *      Author: Samir BEN DODO
 */

#include "euclidean_algorithm.h"
#include "extended_euclidean_algorithm.h"
#include "miller_rabin.h"

int main() {
	euclidean_gcd(1914,899);
	recursive_euclidean_gcd(1914,899,0);
	eea_algorithm(1914,899);
	miller_rabin(1000000099	,10); // composite
	miller_rabin(1000000087	,10); // prime


	return 0;
}
