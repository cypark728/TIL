#include <iostream>
#include <string>

using namespace std;

int main(void){
	int a;
	string str;
	string b;
	int result = 0;
	
	cin >> a;
	cin >> str;
	for(int i=0; i<a; i++){
		b = str[i];
		result = result + stoi(b);
	}
	
	cout << result << endl;
	
	return 0;
}