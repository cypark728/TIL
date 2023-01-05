#include <iostream>

int main(void){
	int count = 0;
	int a, b;
	
	scanf("%d",&count);
	for(int i=0;i<count;i++){
		scanf("%d %d",&a, &b);
		printf("%d\n",a + b);
	}
	
	
	return 0;
}