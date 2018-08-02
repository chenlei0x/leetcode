#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef int bool;


void p(char *s, int len)
{
	int i;
	for (i = 0; i < len; i++) {
		printf("%c", s[i]);
	}
	puts("");
}
bool __helper(char *s1, int len1, char *s2, int len2, char *s3, int len3)
{
	int a = 0, b = 0;
//	printf("s1:");
//	p(s1, len1);
//	printf("s2:");
//	p(s2, len2);
//	printf("s3:");
//	p(s3, len3);
	
	if (len2 == 0 && len1 == 0 && len3 ==0)
		return 1;
	
	if (len1 && len3 && s1[len1 - 1] == s3[len3 - 1]) {
		a = __helper(s1, len1 - 1, s2, len2, s3, len3 - 1);
	}
	if (len2 && len3 && s2[len2 - 1] == s3[len3 - 1]) {
		b = __helper(s1, len1, s2, len2 - 1, s3, len3 - 1);
	}
	
	return a || b;
}
bool isInterleave(char* s1, char* s2, char* s3)
{
	   int len1 = strlen(s1); 
	   int len2 = strlen(s2); 
	   int len3 = strlen(s3); 
	   return __helper(s1, len1, s2, len2, s3, len3);
}


void main()
{
	char *arr[] = {
	};
	char *s1 = arr[0]; 
	char *s2 = arr[1];
	char *s3 = arr[2];
	int a;
	a = isInterleave(s1, s2, s3);
	printf("%d\n", a);
	return;
}
