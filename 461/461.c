#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 

int hammingDistance(int x, int y) 
{
	int i;
	int ret = 0;
	for (i = 0; i < sizeof(int) * 8; i++) {
		int _x = x & (1 << i);
		int _y = y & (1 << i);
		ret += !!(_x ^ _y);
	}
	return ret;
}
int main(int argc, char **argv)
{
}
