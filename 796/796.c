#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 


#define MAX_STR_LEN 40
void **alloc_mem(int size, int m, int n)
{
	void **p;
	int i;
	p = malloc(m * sizeof(void *));
	for (i = 0; i < m; i++) {
		p[i] = malloc(size * n);
	}
	return p;
}
int max_comm_str(char *a, char *b, char **start_a, char **start_b)
{
	int len_a = strlen(a);
	int len_b = strlen(b);
	int **res = (int **)alloc_mem(sizeof(int), len_a, len_b);

	int i, j;
	int max = 0, max_index = 0;
	for (i = 0; i < len_a; i++) {
		for (j = 0; j < len_b; j++) {
			if (a[i] == b[j]) {
				if (i > 0 && j > 0) {
					res[i][j] = res[i-1][j-1] + 1;
				} else if (i == 0 || j ==0){
					res[i][j] = 1;
				}
			} else
				res[i][j] = 0;
			if (max < res[i][j]) {
				max = res[i][j];
				max_index = i - max + 1;
				*start_a = &a[i] - max + 1;
				*start_b = &b[j] - max + 1;

			}
		}
	}

	return max;
}

typedef int bool;
enum {
	false,
	true,
};
bool rotateString(char* a, char* b) {
	int max_comm_str_len;
	char *start_a, *start_b;
	int i, j;

	if (strlen(a) != strlen(b))
		return false;

	max_comm_str_len = max_comm_str(a, b, &start_a, &start_b);
	if (max_comm_str_len == 0) {
		if (a[0] == 0)
			return true;
		return false;
	}

	i = start_a - a + max_comm_str_len;
	j = start_b - b + max_comm_str_len;
	
	while (1) {
		if (a[i] == 0)
			i = 0;
		if (b[j] == 0)
			j = 0;
		if (i == start_a - a || j == start_b - b)
			return true;
		if (a[i] != b[j])
			break;
		i++;
		j++;
	}
	return false;
}
int main()
{
	rotateString("abcde",
"cdeab");
	return 0;
}
