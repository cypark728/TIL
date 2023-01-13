#include <iostream>

using namespace std;

int main(){
    int N, K;
    cin >> N;
    int end = 0;
    int count = 0;
    int inx = 0;

    cin >> K;
    int list[N] = {0};
    int result_list[N];
    printf("<");
    while(true){
        if(list[inx] == 0){
            count ++;
        }

        if(count == K){
            if(end != N-1){
                list[inx] = 1;
                printf("%d, ", inx+1);
                end ++;
                count = 0;
            }else{
                list[inx] = 1;
                printf("%d", inx+1);
                end ++;
                count = 0;
            }
        }

        inx ++;
        if(inx == N){
            inx = 0;
        }
        if(end == N){
            break;
        }
    }
    printf(">");

    return 0;
}