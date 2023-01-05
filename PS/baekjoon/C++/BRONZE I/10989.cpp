#include <iostream>

using namespace std;

int main(){
	
	int count;
	int temp;
	int list[10001] = {0, };
	
	cin >> count;
	for(int i=0; i<count; i++){
		cin >> temp;
		list[temp]++;
	}
	
	for(int i=0; i<10001; i++){
		for(int j=0; j<list[i]; j++){
			cout << i << "\n";
		}
	}
	
	return 0;
}