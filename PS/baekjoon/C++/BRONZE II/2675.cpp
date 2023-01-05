#include <iostream>
#include <string>

using namespace std;

int main(void){
	int a;
	int rep;
	string str;
	
	cin >> a;
	
	for(int i=0; i<a; i++){
		cin >> rep >> str;
		for(int j=0; j<str.size(); j++){
			for(int k=0; k<rep; k++){
				cout << str[j];
			}
		}
		cout << endl;
	}
	
	
	return 0;
}