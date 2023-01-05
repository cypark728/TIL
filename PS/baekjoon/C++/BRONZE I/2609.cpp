#include <iostream>

using namespace std;

int main(void){
	int a, b;
	int x = 0;
	int y;
	int count = 1;
	
	cin >> a >> b;
	y = a * b + 1;
	
	while(count < a*b+1){
		if(a % count == 0 && b % count == 0){
			if(count > x){
				x = count;
			}
		}
		
		if(count % a == 0 && count % b == 0){
			if(count < y){
				y = count;
			}
		}
		
		count ++;
	}
	
	printf("%d\n%d", x, y);
	
	
	
	return 0;
}