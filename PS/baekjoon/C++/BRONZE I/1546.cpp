#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
	float count;
	float list[1000];
	float M = 0;
	float result = 0.0;
	
	cin >> count;
	
	for(int i=0; i<count; i++){
		cin >> list[i];
		M = max(M, list[i]);
	}
	
	for(int i=0; i<count; i++){
		result = result + (list[i] / M * 100);
	}
	
	cout << result / count << endl;
	
	
	
	
	return 0;
}