#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

// Forward declaration of isBadVersion API.
int isBadVersion(int version)
{
	if (version >= 1702766719)
		return 1;
	return 0;
}

int firstBadVersion(int n) {
	int left = 1;
	int right = n;
	int mid;
	if (isBadVersion(1))
		return 1;
	while(left + 1 != right) {
		mid = (right - left) / 2 + left;
		if (isBadVersion(mid))
			right = mid;
		else
			left = mid;
	}
	return right;
    
}
int main()
{
	int ret;
	ret = firstBadVersion(2126753390);
	printf("%d\n", ret);
	
	return 0;
}

