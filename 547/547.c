#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>


struct queue_t {
	int data;
};

int _index;
int queue[300];
void enqueue(int n)
{
	queue[_index++] = n;
}

int dequeue()
{
	return queue[--_index];
}

int size()
{
	return _index;
}

int empty()
{
	return empty > 0;
}

int visited[300] = { 0 };

int findCircleNum(int** M, int MRowSize, int MColSize) 
{
	int i, j;
	int **a = M;
	int n = MRowSize;	
	int t;
	int ret = 0;
	for (t = 0; t < n; t++) {
		if (visited[t] == 1)
			continue;
		enqueue(t);
		visited[t] = 1;
		while(!empty()) {
			int target = dequeue();
			for (i = 0; i < n; i++) {
				if(i != target && a[i][target] == 1 && visited[i] == 0)
					visited[target] = 1;
					enqueue(i);
			}
		}
		ret++;
		
	}
}

int main()
{
	int ret;

}

