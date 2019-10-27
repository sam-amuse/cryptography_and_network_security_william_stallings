/*
 * main.cpp
 *
 *  Created on: 27 oct. 2019
 *      Author: Samir BEN DODO
 */

#include "euclidean_algorithm.h"
#include "extended_euclidean_algorithm.h"

int main() {
	euclidean_gcd(1914,899);
	recursive_euclidean_gcd(1914,899);
	eea_algorithm(1914,899);
	return 0;
}
