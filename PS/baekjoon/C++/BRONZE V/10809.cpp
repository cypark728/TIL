#include <iostream>
#include <string>

using namespace std;

int main(void){
	string str;
	int alp[26];
	
	fill_n(alp, 26, -1);
	cin >> str;
	for(int i=0; i<str.size(); i++){
		if(alp[int(str[i]) - 97] == -1){
			alp[int(str[i]) - 97] = i;
		}
	}
	
	for(int i=0; i<26; i++){
		cout << alp[i] << " ";
	}
	
	
	return 0;
}