#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define min(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a < _b ? _a : _b;	  \
	 }) 

#define max(a, b) \
	({ __typeof__(a) _a = (a);  \
	__typeof__(b) _b = (b);  \
   _a > _b ? _a : _b;	  \
	 }) 

#define min_node(a, b) \
	a->val > b->val ? b : a

struct ListNode {
    int val;
    struct ListNode *next;
};
 

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) 
{
	struct ListNode *l;
	int i, min_i;
	struct ListNode new;
	struct ListNode **tail = &new.next;
	struct ListNode *min;
	struct ListNode *tmp;
	int should_finish = 0;	
	*tail = NULL;
	
	while (!should_finish) {
		min = NULL;
		should_finish = 1;
		for (i = 0; i < listsSize; i++) {
			tmp = lists[i];	
			if (!tmp)
				continue;
			should_finish = 0;
			if (!min) {
				min = tmp;
				min_i = i;
			} else if (min->val > tmp->val) {
				min = tmp;
				min_i = i;
			}
		}
		if (should_finish)
			break;
		lists[min_i] = min->next;
		min->next = NULL;
		*tail = min;
		tail = &min->next;
	}
	return new.next;
}


struct ListNode *array_to_list(int *a, int len)
{
	int i;
	struct ListNode *ret;
	struct ListNode **tail;
	struct ListNode *tmp;
	tail = &ret;

	for (i = 0; i < len; i++) {
		if (!a[i])
			continue;
		tmp = malloc(sizeof(struct ListNode));
		tmp->val = a[i];
		tmp->next = NULL;
		*tail = tmp;
		tail = &tmp->next;
	}
	return ret;
}

void print_list(struct ListNode *list)
{
	struct ListNode *p = list;
	while (p) {
		printf("%d--->", p->val);	
		p = p->next;
	}
	printf("\n");
}

int a[][3] = {
	{1, 4, 5},
	{1, 3, 4},
	{2, 6},
};
void main()
{
	int ret;
	int (*pa)[3] = a;
	struct ListNode *test;
	struct ListNode **array = malloc(sizeof(struct ListNode *) * 3);
	int i;
	for (i = 0; i < 3; i++) {
		array[i] = array_to_list(pa[i], 3);
		print_list(array[i]);
	}

	test = mergeKLists(array, 3);
	print_list(test);
	
	//printf("%d\n", maxArea(a, numSize));
}
