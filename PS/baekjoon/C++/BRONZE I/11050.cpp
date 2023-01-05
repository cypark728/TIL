#include <iostream>

using namespace std;

int factorial(int a);

int main(void){
	int n, k;
	int result;
	
	cin >> n >> k;
	result = factorial(n)/(factorial(k)*(factorial(n-k)));
	cout << result << endl;
	
	return 0;
}

int factorial(int a){
	int result = 1;
	if(a <= 1){
		result = 1;
	}else{
		for(int i=1; i<=a; i++){
			result = result * i;
		}
	}
	
	return result;
}