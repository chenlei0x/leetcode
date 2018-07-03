#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 

typedef unsigned int uint32_t;
int hammingWeight(uint32_t n) {
	int ret = 0;
	while(n) {
		n &= n - 1;
		ret++;
	}

	return ret;

}
int main(int argc, char **argv)
{
	hammingWeight(1);
	printf()
}
