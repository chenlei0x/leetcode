#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 

int maxArea(int* height, int heightSize) 
{
	int left, right;
	int i, j;
	int max;
	
	i = 0;
	j = heightSize -1;
	left = height[i];
	right = height[j];
	max = min(left, right) * j;

	while(i < j)
	{
		if (left < right) {
			i++;
			if (left > height[i])
				continue;
		} else {
			j--;
			if (right > height[j])
				continue;
		}
		left = height[i];
		right = height[j];
		int s = min(left, right) * (j - i);
		if ( s > max)
			max = s;
	}
	return max;
}
void main()
{
	int ret;
	int a[] = {1,2};
	int numSize = sizeof(a)/sizeof(a[0]);
	printf("%d\n", maxArea(a, numSize));
}
