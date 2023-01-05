#include <iostream>
#include <string>

using namespace std;

int main(void){
	int count;
	int bef = 0;
	int result = 0;
	string str;
	string s;
	
	cin >> count;
	for(int i=0; i<count; i++){
		cin >> str;
		for(int j=0; j<str.size(); j++){
			s = str[j];
			if(s.compare("O") == 0){
				bef ++;
				result = result + bef;
			}else{
				bef = 0;
			}
		}
		cout << result << endl;
		result = 0;
		bef = 0;
	}
	
	
	return 0;
}