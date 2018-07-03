#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int findComplement(int num)
{
	int mask = ~0;
	while(num & mask)	
		mask <<= 1;
	return ~num & ~mask;
}


int main()
{
	char **ret;
	int size;
	int i;
	ret = generateParenthesis(4, &size);
	
	for (i = 0; i < size; i++)
		printf("[%d]%s  \n", i, ret[i]);
	return 0;
}
