#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 

#define max(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a > _b ? _a : _b;	  \
	 }) 

#define min_node(a, b) \
	a->val > b->val ? b : a

void swap(int *a, int i, int j)
{
	int tmp;
	tmp = a[i];
	a[i] = a[j];
	a[j] = tmp;
}

int removeElement(int* nums, int numsSize, int val) 
{
	int i, j;
	int *a = nums;
	int count;
	i = 0;
	j = numsSize - 1;
	
	
	if (numsSize == 0)
		return 0;
	if (numsSize == 1)
		return nums[0] != val;
	while (i < numsSize) {
		while (a[i] != val && i < numsSize) {
			i++;
		}
		if (i == numsSize)
			break;
		count++;
		for (j = i+1; j < numsSize && a[j] == val; j++);
		if (j == numsSize)
			break;
		else
			swap(a, i, j);
	}
	return i;
}



void main()
{
	int ret;
	//int a[] = {0,1,2,2,3,0,4,2};
	int a[] = {3,3};
	int len = sizeof(a)/sizeof(a[0]);
	int i;
	ret = removeElement(a, len, 3);
	printf("ret - %d\n", ret);

	for (i = 0; i < ret; i++)
		printf("%d  \n", a[i]);

}

