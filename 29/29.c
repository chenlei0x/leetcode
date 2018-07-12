#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>


int divide(int dividend, int divisor)
{
	int ret = 0;
	int i;
	int sign_1 = (dividend < 0);
	int sign_2 = (divisor < 0);
	int sign = sign_1 ^ sign_2;
	long long _dividend = labs(dividend);
	long long _divisor = labs(divisor);
	if (dividend == INT_MIN && divisor == -1)
		return INT_MAX;
	while(_dividend >= _divisor) {
		for (i = 0; _dividend >= (_divisor << i) ;i++);
		_dividend -= (_divisor << (i-1));
		ret += 1 << (i-1);
	}
	if (sign)
		return -ret;
	return ret;
}
int main(int argc, char **argv)
{
	int ret;	
	ret = divide(1, 1);
	printf("%d\n", ret);
	return 0;
}
