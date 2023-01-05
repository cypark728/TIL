#include <iostream>

int main(void){
	int count;
	int list[100];
	int check;
	int result = 0;
	
	scanf("%d",&count);
	for(int i=0; i<count; i++){
		scanf("%d", &list[i]);
	}
	scanf("%d", &check);
	
	for(int i=0; i<count; i++){
		if(check == list[i]){
			result ++;
		}
	}
	
	printf("%d", result);
	
	
	
	return 0;
}