#include <iostream>
#include <algorithm>

using namespace std;

struct TEMP{
    int x;
    int y;
};

bool compare(TEMP &p1, TEMP&p2){
    if(p1.x == p2.x){
        return p1.y < p2.y;
    }else{
        return p1.x < p2.x;
    }
}

int main (){
    int N;
    cin >> N;
    TEMP temp[N];

    for(int i=0; i<N; i++){
        cin >> temp[i].x;
        cin >> temp[i].y;
    }

    sort(temp, temp+N, compare);

    for(int j=0; j<N; j++){
        printf("%d %d\n", temp[j].x, temp[j].y);
    }

    return 0;
}