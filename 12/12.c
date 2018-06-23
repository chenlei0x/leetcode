#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define __DEBUG

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

struct group roman_table[] = {{"I", "V"}, {"X", "L"}, {"C", "D"}, {"M"}};
int roman_table_len = sizeof(roman_table) / sizeof(roman_table[0]);


int num_to_roman(int level, int num, char *buf)
{
	int i;
	int ret = 0;
	if (level >= roman_table_len)
		return -1;
	struct group *g = &roman_table[level];
	switch (num) {
	case 0 ... 3:
		for (i = 0; i < num; i++)
			strcat(buf, g->one);
		break;
	case 4:
		sprintf(buf, "%s%s", g->one, g->five);
		break;
	case 5 ... 8:
		sprintf(buf, "%s", g->five);
		for (i = 5; i < num; i++)
			strcat(buf, g->one);
		break;
	case 9:
		sprintf(buf, "%s", g->nine);
		break;
	default:
		ret = -1;
		break;
	}
#ifdef __DEBUG
	printf("[%s]", buf);
#endif
	return ret;
}
char* intToRoman(int num)
{
	char *ret = malloc(100);
	char *tmp;
	int i;
	int d = 100000;
	char buf[16];
	memset(buf, 0, sizeof(buf));

	for (i = 0; i < sizeof(roman_table)/sizeof(roman_table[0]) - 1; i++) {
		tmp = malloc(3);
		sprintf(tmp, "%s%s", roman_table[i].one, roman_table[i+1].one);
		roman_table[i].nine = tmp;
	}

	i = 5;

	int digit;
	for (i = 5, d = 100000; i >= 0; i--, d /= 10) {
		digit = num / d;
		if (!digit)
			continue;
		num_to_roman(i, digit, buf);
		strcat(ret, buf);
		buf[0] = '\0';
		num = num % d;
	}
	return ret;
}


int main(int argc, char **argv)
{
	int n = 11;
	char *p = intToRoman(n);
	printf("%s\n", p);
	return 0;
}

