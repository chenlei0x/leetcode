#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int find_min(int *num, int *a, int target)
{
	int i;
	int min = INT_MAX;
	int steps;
	for (i = 0; i < target; i++) {
		steps = target - i;
		if (num[i] >= steps && a[i] < min) {
			min = a[i];
		}
	}
	return min + 1;
}

int jump(int* nums, int numsSize) 
{
	int *a = calloc(numsSize, sizeof(int));
	int i;
	int ret;
	memset(a, numsSize*sizeof(int), 0);

	for (i = 1; i < numsSize; i++) {
		a[i] = find_min(nums, a, i);
	}
	ret = a[i-1];
	free(a);
	return ret;
}

void main()
{
	int ret;
	int a[] = {4,1,1,3,1,1,1};
	int numSize = sizeof(a)/sizeof(a[0]);
	ret = jump(a, numSize);
	printf("%d\n", ret);
}
