#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int N;
    cin >> N;
    int list[N];
    for(int i = 0; i < N; i++){
        scanf("%d ", &list[i]);
    }
    sort(list, list + N);

    int M;
    cin >> M;
    int temp;
    int low = 0;
    int high = N ;
    int mid = 0;
    for(int j = 0; j < M; j++){
        scanf("%d", &temp);
        low = 0;
        high = N;
        while(true){
            mid = (low + high) / 2;
            if(list[mid] == temp){
                printf("1\n");
                break;
            }
            else if(list[mid] < temp){
                low = mid + 1;
            }
            else if(list[mid] > temp){
                high = mid - 1;
            }

            if(low > high){
                printf("0\n");
                break;
            }
        }
    }




    return 0;
}