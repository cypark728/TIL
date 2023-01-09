#include <iostream>

using namespace std;

int main (){
    int N;
    int cur;
    int temp = 0;
    int result = 0;

    cin >> N;
    for(int i=0; i<N; i++){
        cin >> cur;
        if(cur != 1){
            for(int j=2;j<cur;j++){
                if(cur % j == 0){
                    temp ++;
                }
            }
            
            if(temp == 0){
                result ++;
            }
        }
        temp = 0;
    }
    cout << result << endl;



    return 0;
}