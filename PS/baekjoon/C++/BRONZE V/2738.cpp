#include <iostream>

int main(void){
	int a[100][100];
	int b[100][100];
	int c[100][100];
	int x = 0;
	int y = 0;
	
	scanf("%d %d", &x, &y);
	
	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			scanf("%d ", &a[i][j]);
		}
	}
	
	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			scanf("%d", &b[i][j]);
		}
	}
	
	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			c[i][j] = a[i][j] + b[i][j];
		}
	}
	
	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			printf("%d ", c[i][j]);
		}
		printf("\n");
	}
	
	
	
	
	return 0;
}