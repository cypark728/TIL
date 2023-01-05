#include <iostream>

using namespace std;

int main(void){
	int count;
	int check_count = 0;
	int n,k;
	int list[15][15];
	
	cin >> count;
	while(check_count < count){
		cin >> k;
		cin >> n;
		for(int i=1; i<=n; i++){
			list[0][i] = i;
		}
		for(int i = 1; i<=k; i++){
			for(int j=1; j<=n; j++){
				if(j == 1){
					list[i][j] = 1;
				}else{
					list[i][j] = list[i][j-1] + list[i-1][j];
				}
			}
		}
		cout << list[k][n] << endl;
		check_count ++;
	}
	
	
	return 0;
}