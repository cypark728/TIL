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


	//����Ʈ�� ��Ʈ�� �ޱ�, ���� �ε����� ���� ��Ʈ���� ���� ����
	for(int i=0; i<count; i++){
		cin >> list[i];
		length[i] = list[i].length();               
	}

	//���̿� ���� ��Ʈ�� ����Ʈ�� ���� ����Ʈ�� �����Ʈ
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
	
	
	//���̰� �����ÿ� ���ĺ� ������ �ٽ� ����
	for(int i=1; i<count; i++){
		if(i == count - 1 || length[i] != length[i-1]){
			sort(list+sort_temp, list+i);
			sort_temp = i;
		}
	}

	//���� ���
	for(int i=0; i<count; i++){
		if(i == 0){
			cout << list[i] << endl;
		}else if(list[i].compare(list[i-1]) != 0){
			cout << list[i] << endl;
		}
	}
	
	
	
	return 0;
}