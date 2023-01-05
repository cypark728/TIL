#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main(void){
	int n;
	string str;
	long long result = 0;
	long long m = 1234567891;
	
	cin >> n;
	cin >> str;
	for(int j=0; j<str.size(); j++){
		result = result + (long(str[j]) - 96) * (pow(31, j));
	}
	
	cout << result % m << endl;
	
	
	return 0;
}