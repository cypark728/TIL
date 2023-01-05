#include <iostream>

using namespace std;

int main(void){
	int inp;
	int temp = 0;
	int rev = 0;
	
	
	while(true){
		cin >> inp;
		temp = inp;
		if(inp == 0){
			break;
		}else{
			while(temp != 0){	
				rev = rev*10 + temp % 10;
				temp = temp / 10;
			}
			if(inp == rev){
				cout << "yes" << endl;
			}else{
				cout << "no" << endl; 
			}
		}
		rev = 0;
		temp = 0;
	}
	
	
	return 0;
}