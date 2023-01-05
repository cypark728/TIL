#include <iostream>
#include <string>

using namespace std;

int main(void){
	string str;
	int alp[26] = {};
	int max = 0;
	int imax;
	int scheck = 0;

	cin >> str;
	for(int i=0; i<str.size(); i++){
		if(int(str[i]) > 90){
			alp[(int(str[i]) - 97)]++;
		}else{
			alp[(int(str[i]) - 65)]++;
		}
	}
	
	for(int i=0; i<26; i++){
		if(alp[i] > max){
			max = alp[i];
			imax = i;
		}
	}
	
	for(int i=0; i<26; i++){
		if(alp[i] == max){
			scheck ++;
		}
	}
	
	if(scheck == 1){
		cout << char(imax + 65) << endl;	
	}else{
		cout << "?" << endl;
	}
	
	return 0;
}