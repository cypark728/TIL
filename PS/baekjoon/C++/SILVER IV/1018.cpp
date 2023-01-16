#include <iostream>
#include <string>

using namespace std;

string WB[8] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
};
string BW[8] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
};



int main(){
    int M, N;
    int min = 9999999;
    int temp = 0;
    int sur_x = 0;
    int sur_y = 0;

    cin >> M >> N;

    string board[M];

    for(int i=0; i<M; i++){
        cin >> board[i];
    }

    for(int x=0; x<=M-8; x++){
        for(int y=0; y<=N-8; y++){
            for(int i=x; i<x+8; i++){
                for(int j=y; j<y+8; j++){
                    if(board[i][j] != WB[sur_x][sur_y]){
                        temp += 1;
                    }
                    sur_y += 1;
                }       
                sur_y = 0;
                sur_x += 1;
            }
            sur_x = 0;
            sur_y = 0;
            if(temp < min){
                min = temp;
            }
            temp = 0;
            for(int q=x; q<x+8; q++){
                for(int w=y; w<y+8; w++){
                    if(board[q][w] != BW[sur_x][sur_y]){
                        temp += 1;
                    }
                    sur_y += 1;
                }    
                sur_y = 0;   
                sur_x += 1;
            }
            sur_x = 0;
            sur_y = 0;
    
            if(temp < min){
                min = temp;
            }
            temp = 0;
        }
    }



    printf("%d", min);


    return 0;
}