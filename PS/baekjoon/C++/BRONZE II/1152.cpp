#include <iostream>
#include <string>

using namespace std;

int main(void){
	string str;
	int result = 0;
	string check;
	
	getline(cin, str);
	for(int i=0; i<str.size(); i++){
		check = str[i];
		if(check.compare(" ") == 0){
			result ++;
		}
	}
	
	check = str[0];
	if(check.compare(" ") == 0){
		result --;
	}
	
	check = str[(str.size() - 1)];
	if(check.compare(" ") == 0){
		result --;
	}
	
	cout << result + 1 << endl;
	
	
	return 0;
}