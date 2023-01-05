#include <iostream>
#include <string>

using namespace std;

int main(void){
	string a, b;
	string n = "000", m = "000";
	
	cin >> a >> b;
	
	n[0] = a[2];
	n[1] = a[1];
	n[2] = a[0];
	
	m[0] = b[2];
	m[1] = b[1];
	m[2] = b[0];
	
	if(n > m){
		cout << n << endl;
	}else{
		cout << m << endl;
	}
	
	
	return 0;
}