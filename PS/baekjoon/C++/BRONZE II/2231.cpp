#include <iostream>
#include <math.h>

using namespace std;

int main(void){
	int a;
	int temp = 0;
	int temp2 = 0;
	int check = 0;
	
	cin >> a;
	for(int i=1; i<a; i++)
	{
		temp2 = i;
		while(temp2 != 0){
			temp = temp + temp2 % 10;
			temp2 = temp2 / 10;
		}
		temp = temp + i;
		if(temp == a){
			cout << i << endl;
			check = 1;
			break;
		}else{
			temp = 0;
		}
	}
	
	if(check == 0){
		cout << "0" << endl;
	}
	
	
	
	return 0;
}