#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void){
	int count;
	
	cin >> count;
	
	string list[count];
	for(int i=0; i<count; i++){
		cin >> list[i];
	}
	
	sort(list, list+count);
	
	for(int i=0; i<count; i++){
		cout << list[i] << endl;
	}
	
	
	
	return 0;
}