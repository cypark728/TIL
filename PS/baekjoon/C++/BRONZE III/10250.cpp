#include <iostream>

using namespace std;

int main(void){
	int a;
	int count;
	int w, h;
	int temp = 1;
	
	cin >> a;
	
	for(int i=0; i<a; i++){
		cin >> h >> w >> count;
		for(int j = 1; j <= w; j++){
			for(int k = 1; k <= h; k++){
				if(temp == count){
					cout << 100 * k + j << endl;
					temp ++;
				}else{
					temp++;
				}
			}
		}
		temp = 1;
	}
	
	
	
	
	return 0;
}