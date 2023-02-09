#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool compare(string p1, string p2){
    if(p1.length() == p2.length()){
        return p1 < p2;
    }else{
        return p1.length() < p2.length();
    }
}

int main (){
	int N;
	cin >> N;
	string list[N];

	for(int i=0; i < N; i++){
		cin >> list[i];
	}

	sort(list, list + N, compare);

	for(int j=0; j < N; j++){
		if(j != 0){
			if(list[j - 1] != list[j]){
				cout << list[j] << "\n";
			}
		}else{
			cout << list[j] << "\n";
		}
	}



	return 0;
}