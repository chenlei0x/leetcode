#include <stdio.h>


void print_array(int *a, int len)
{
	int i;
	for (i = 0; i < len; i++) {
		printf("%d  ", a[i]);	
	}
	printf("\n");
}

void bubble_sort(int *a, int len)
{
	int i, j;
	for (i = len - 1; i > 0; i--)
		for (j = 0; j < i; j++) {
			printf("j = %d, j+1= %d\n", j, j+1);
			if (a[j] > a[j+1]) {
				int tmp;
				tmp = a[j+1];
				a[j+1] = a[j];
				a[j] = tmp;
			}
		}
}

void insertion_sort(int *a, int len)
{
	int i, j;
	int tmp;
	for (i = 1; i < len; i++) {
		tmp = a[i];
		for (j = i; j > 0 && a[j-1] > tmp; j--)
			a[j] = a[j-1];
		a[j] = tmp;
	}
}

void swap(int *a, int i, int j)
{
	int tmp;
	tmp = a[i];
	a[i] = a[j];
	a[j] = tmp;
}

void print_array_sp(int *a, int len, int sp)
{
	int i;
	for (i = 0; i < len; i++)
		if (i == sp)
			printf("[%d]  ", a[i]);
		else
			printf("%d  ", a[i]);
	printf("\n");
}
void _qsort(int *a, int begin, int end)
{
	int i, j;
	int mid = a[end];
	i = begin, j = end;
	printf("%d --- %d\n", begin, end);
	if (begin >= end)
		return;
	

	print_array(a, end + 1);
	while (i < j) {
		while (a[i] <= mid && i < j)	
			i++;
		a[j] = a[i];
		//print_array_sp(a, end + 1, j);
		while (a[j] >= mid && i < j)
			j--;
		a[i] = a[j];
		//print_array_sp(a, end + 1, i);
	}
	a[i] = mid;
	_qsort(a, begin, i-1);
	_qsort(a, i+1, end);
}

void qsort(int *a, int len)
{
	_qsort(a, 0, len - 1);
}

void main()
{
	int a[] = {5, 9 ,1, 3, 5, 0, 10, 8};	
	int len = sizeof(a)/sizeof(a[0]);
	//bubble_sort(a, len);
	//insertion_sort(a, len);
	qsort(a, len);
	print_array(a, len);
}
