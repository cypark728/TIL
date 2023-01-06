#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void){
	int count;
	
	cin >> count;
	
	string list[count];
	int length[count];
	int int_temp = 0;
	string string_temp;
	int start = 0;
	int sort_temp = 0;


	//리스트에 스트링 받기, 같은 인덱스에 받은 스트링의 길이 저장
	for(int i=0; i<count; i++){
		cin >> list[i];
		length[i] = list[i].length();               
	}

	//길이에 따라서 스트링 리스트와 길이 리스트를 버블소트
	for(int i=0; i<count; i++){
		for(int j=0; j<count -1 - i;j++){
			if(length[j] > length[j+1]){
				int_temp = length[j];
				length[j] = length[j+1];
				length[j+1] = int_temp;

				string_temp = list[j];
				list[j] = list[j+1];
				list[j+1] = string_temp;
			}
		}
	}
	
	
	//길이가 같을시에 알파벳 순서로 다시 정리
	for(int i=1; i<count; i++){
		if(i == count - 1 || length[i] != length[i-1]){
			sort(list+sort_temp, list+i);
			sort_temp = i;
		}
	}

	//값을 출력
	for(int i=0; i<count; i++){
		if(i == 0){
			cout << list[i] << endl;
		}else if(list[i].compare(list[i-1]) != 0){
			cout << list[i] << endl;
		}
	}
	
	
	
	return 0;
}