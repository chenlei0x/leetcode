#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int searchInsert(int* nums, int numsSize, int target) 
{
	int left, right;
	int mid;
	left = 0;
	right = numsSize - 1;
	while (left < right) {
		mid = (left + right) / 2;
		if (nums[mid] > target)
			right = mid - 1;
		else if (nums[mid] < target)
			left = mid + 1;
		else
			return mid;
			
	}
	if (nums[left] < target)
		left++;
	return left;
}


int main()
{
	int a[] = {1,3,5,6};	
	int ret;
	ret = searchInsert(a, sizeof(a)/sizeof(a[0]), 5);
	printf("%d\n", ret);
	ret = searchInsert(a, sizeof(a)/sizeof(a[0]), 2);
	printf("%d\n", ret);
	ret = searchInsert(a, sizeof(a)/sizeof(a[0]), 7);
	printf("%d\n", ret);
	ret = searchInsert(a, sizeof(a)/sizeof(a[0]), 0);
	printf("%d\n", ret);
	return 0;
}

