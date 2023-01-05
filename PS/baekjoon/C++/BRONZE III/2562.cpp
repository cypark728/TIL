#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
	int a[9];
	int b[9];
	int c=0;
	int check = -1;
	
	for(int i=0;i<9;i++){
		scanf("%d",&c);
		a[i] = c;
		b[i] = c;
	}
	sort(a,a+9);
	c = a[8];
	for(int i=0; i<9; i++){
		if(c == b[i]){
			check = i + 1;
		}
	}
	printf("%d\n",c);
	printf("%d",check);
	
	return 0;
}