#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>


void string_cmb(char *s1, char* s2, char *dst)
{
	sprintf(dst, "%s%s", s1, s2);
}


int alloc_mem(char **dst, int size, int str_size)
{
	if (dst == NULL)
		return 0;
	void *buf;
	buf = malloc(size * str_size);
	int i;
	for (i = 0; i < size; i++)
		dst[i] = buf + (i * str_size);
	return size * str_size;
}

void print_str_array(char **a, int len)
{
	int i;
	printf("[%d]\n", len);
	for (i = 0; i < len; i++) {
		puts(a[i]);
	}
	
}

int get_total_strs(int n)
{
	int i;
	int ret = 1;
	for (i = 1; i < n; i++) {
		ret = ret * 3 - 1;
	}
	return ret;
}

#define square(n, _pow)  ({  \
		int i; \
		int ret = 1; \
		for (i = 0; i < _pow; i++) \
		ret *= n; \
		ret; \
})
#if 0
#define HASH_TABLE_LEN 128
unsigned long
hash(unsigned char *str)
{
	unsigned long hash = 5381;
	int c;

	while (c = *str++)
		hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

	return hash;
}


struct hlist_node {
	void *data;
	hlist_node *next;
};

void filter(char **a, int len)
{
	struct hlist_node *hash_table[HASH_TABLE_LEN];
	int hash;
	int i;
	char *p;
	struct hlist_node *node;
	memset(hash_table, sizeof(hash_table), 0);
	for (i = 0; i < len; i++) {
		p = a[i];
		hash = _hash(p) % HASH_TABLE_LEN;
		node = malloc(sizeof(struct hlist_node));
		node->next = hash_table[hash];
		hash_table[hash] = node;
		node->data = p;
		node = NULL;
	}
	for (i = 0; i < HASH_TABLE_LEN; i++) {
		node = hash_table[i];
		if (!node)
			continue;
		while (!node) {
				
		}
	}
}
#endif
int _generate(char *s, int n, int left, int right)
{
	if (strlen(s) == n << 1)		
}

char** generateParenthesis(int n, int* returnSize)
{
	int left = 0; right = 0;
	int s = "";
	_
	if (left < n)

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
//
//	compare(output, expected);
//	if_recurred(output, sizeof(output)/sizeof(output[0]));
//	return 0;
}

char *output[] = {
	"()()()()",
	"(()()())",
	"()(()())",
	"(()())()",
	"((()()))",
	"()()(())",
	"()(())()",
	"(()(()))",
	"()(())()",
	"(())()()",
	"((())())",
	"()((()))",
	"((()))()",
	"(((())))"
};

char *expected[] = {
	"(((())))",
	"((()()))",
	"((())())",
	"((()))()",
	"(()(()))",
	"(()()())",
	"(()())()",
	"(())(())",
	"(())()()",
	"()((()))",
	"()(()())",
	"()(())()",
	"()()(())",
	"()()()()"
};
void compare(s1, s2)
{
	char *p;
	int len = sizeof(expected)/sizeof(expected[0]);
	int i;
	for (i = 0; i < len; i++) {
		p = expected[i];
		int j;
		for (j = 0; j < len; j++) {
			if (strcmp(p, output[j]) == 0)
				break;
		}
		if (j != len)
			continue;
		printf("not found %s\n", p);
		return;
	}
	printf("equal\n");
}

void if_recurred(char **a, int len)
{
	char *p;
	int i;
	for (i = 0; i < len; i++) {
		p = a[i];	
		int j;
		for (j = 0; j < len; j++) {
			if (j == i)	
				continue;
			if (strcmp(a[j], p) == 0) {
				printf("recurred %s %d %d\n", p, i, j);
				return;
			}
		}
	}
}


