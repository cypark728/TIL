#include <iostream>

using namespace std;

int main(){
    int K, N;
    long long low = 1;
    long long high = 1;
    cin >> K >> N ;

    int list[K];
    for(int i=0; i < K; i++){
        cin >> list[i];
        if(high < list[i]){
            high = list[i];
        }
    }
    long long mid;
    int temp = 0;
    int ans = 0;
    while(low <= high){
        temp = 0;
        mid = (low + high) / 2;
        for(int j = 0; j < K; j++){
            temp = temp + (list[j] / mid);
        }

        if(temp < N){
            high = mid - 1;
        }
        else if(temp >= N){
            low = mid + 1;
            if(ans < mid){
                ans = mid;
            }
        }
    }
    cout << ans;




    return 0;
}