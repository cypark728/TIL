#include <iostream>

using namespace std;

int main(void){
	int a;
	int result = 0;
	
	for(int i=0; i<5; i++){
		cin >>a;
		result = result + (a * a);
	}
	
	cout << result%10 << endl;
	
	return 0;
}