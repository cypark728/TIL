#include <iostream>

int main(void){
	long long n,m;
	
	scanf("%lld %lld",&n, &m);
	
	long long score = n - m;
	
	if(score<0){
		score = score * -1;
	}
	
	printf("%lld",score);
	
	return 0;
}