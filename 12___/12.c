#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

struct group {
	char *one;
	char *five;
	char *nine;
};


int level(int n, int *digit)
{
	int i;
	int pow = 10;
	for (i = 0; i < 5; i++) {
		if (n / pow == 0)
			*digit = n % pow;
			return i;
	}
	return 0;
}


char* intToRoman(int num)
{
	char ret[100];
	char *tmp;
	struct group g[] = {{"I", "V"}, {"X", "L"}, {"C", "D"}, {"M"}};
	int i;
	for (i = 0; i < sizeof(g)/sizeof(g[0]) - 1; i++)) {
		tmp = malloc(3);
		sprintf(tmp, "%s%s", g[i].one, g[i+1].one);
		g[i].nine = tmp;
	}

	int level;
	while(num) {
		level = level(num);
		num /= 10;
	}
	return ret;
}

cha

int main()
{
	return 0;
}

