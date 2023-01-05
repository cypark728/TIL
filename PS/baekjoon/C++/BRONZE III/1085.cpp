#include <iostream>

using namespace std;

int main(void){
	int x, y, w, h;
	int min = 10000;
	
	cin >> x >> y >> w >> h;
	
	if(w - x < min){
		min = w - x;
	}
	if(h - y < min){
		min = h - y;
	}
	if(x < min){
		min = x;
	}
	if(y < min){
		min = y;
	}
	
	cout << min << endl;
	
	return 0;
}